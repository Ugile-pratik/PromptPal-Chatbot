from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import json
import os

app = Flask(__name__)

# Placeholder for chatbot's learned knowledge and chat history
learned_data = {}
chat_history = []

# Path to the JSON file for storing learned data
LEARNED_DATA_FILE = 'learned_data.json'

# Load learned data from the JSON file if it exists
def load_learned_data():
    global learned_data
    if os.path.exists(LEARNED_DATA_FILE):
        with open(LEARNED_DATA_FILE, 'r') as file:
            learned_data = json.load(file)

# Save learned data to the JSON file
def save_learned_data():
    with open(LEARNED_DATA_FILE, 'w') as file:
        json.dump(learned_data, file)

# Initialize the vectorizer and k-NN model
vectorizer = TfidfVectorizer()
knn_model = NearestNeighbors(n_neighbors=1)

# Function to train the k-NN model
def train_knn_model():
    if learned_data:
        inputs = list(learned_data.keys())
        vectors = vectorizer.fit_transform(inputs)
        knn_model.fit(vectors)

# Function to get the best response based on k-NN and keyword matching
def get_best_response(user_input):
    if not learned_data:
        return None  # No learned responses to compare with

    # Keyword Matching
    for key in learned_data.keys():
        if key in user_input:
            return learned_data[key]

    # Vector Space Model using k-NN
    user_vector = vectorizer.transform([user_input])
    distances, indices = knn_model.kneighbors(user_vector)

    if distances[0][0] < 0.1:  # Threshold for relevance
        return learned_data[list(learned_data.keys())[indices[0][0]]]

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn-page')
def learn_page():
    return render_template('learn.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', chat_history=chat_history, learned_data=learned_data)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message').lower()
    print(f"Received input: {user_input}")  # Debugging output

    chat_history.append(f"User: {user_input}")

    response = get_best_response(user_input)
    
    if response is None:
        if user_input == 'text to speech':
            response = "Text to Speech activated. Type 'exit' to return."
        elif user_input == 'text to image':
            response = "Text to Image activated. Type 'exit' to return."
        elif user_input == 'exit':
            response = "Exited from the current feature. Continue chatting."
        else:
            response = "I don't know the answer. Please provide the correct answer."

    print(f"Response: {response}")  # Debugging output
    chat_history.append(f"Chatbot: {response}")
    return jsonify({"response": response})

@app.route('/learn', methods=['POST'])
def learn():
    user_input = request.json.get('user_input').lower()
    correct_answer = request.json.get('correct_answer')
    
    learned_data[user_input] = correct_answer
    print(f"Learning: {user_input} -> {correct_answer}")  # Debugging output

    # Save the updated learned data to file
    save_learned_data()

    if learned_data:
        train_knn_model()
    
    return jsonify({"status": "Learned successfully!"})

@app.route('/delete-learned-data', methods=['POST'])
def delete_learned_data():
    user_input = request.json.get('user_input')
    if user_input in learned_data:
        del learned_data[user_input]
        print(f"Deleted learned data for: {user_input}")  # Debugging output
        
        # Save the updated learned data to file
        save_learned_data()

        return jsonify({"status": "Learned data deleted successfully!"})
    return jsonify({"status": "User input not found!"})

@app.route('/clear-chat-history', methods=['POST'])
def clear_chat_history():
    global chat_history
    chat_history = []  # Clear the chat history
    print("Chat history cleared.")  # Debugging output
    return jsonify({"status": "Chat history cleared successfully!"})

# Route to modify learned data
@app.route('/modify-learned-data', methods=['POST'])
def modify_learned_data():
    user_input = request.json.get('user_input')
    new_answer = request.json.get('new_answer')

    if user_input in learned_data:
        learned_data[user_input] = new_answer
        print(f"Modified: {user_input} -> {new_answer}")  # Debugging output
        
        # Save the updated learned data to file
        save_learned_data()

        return jsonify({"status": "Learned data modified successfully!"})
    
    return jsonify({"status": "User input not found!"})

if __name__ == '__main__':
    load_learned_data()  # Load data when starting the app
    app.run(debug=True)
