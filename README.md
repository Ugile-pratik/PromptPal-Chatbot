
### Project Description

**PromptPal** is an intelligent, self-learning chatbot built with Python and Flask. Unlike static chatbots, 
PromptPal uses a combination of keyword matching and a **k-Nearest Neighbors (k-NN)** machine learning model to provide relevant responses. 
A key feature of the project is its ability to "learn" in real-time; if the bot doesn't know an answer, it prompts the user for the correct one and stores it for future interactions. 
The project also includes a dedicated Admin Panel for managing learned data and viewing chat history.

---
* **Architecture: Client-Server Model**
The project follows a standard web architecture where the **Flask** backend acts as the server and the browser acts as the client. The client sends asynchronous requests using the **Fetch API** in JavaScript to the `/chat` or `/learn` endpoints, allowing the UI to update without refreshing the page.
* **Natural Language Processing (NLP): TF-IDF Vectorization**
The bot uses `TfidfVectorizer` to convert text into numerical vectors.
* **Term Frequency (TF):** Measures how frequently a term occurs in a document.
* **Inverse Document Frequency (IDF):** Reduces the weight of terms that appear very frequently across all documents (like "is" or "the") and increases the weight of terms that are unique and carry more meaning.


* **Machine Learning: k-Nearest Neighbors (k-NN)**
The core "intelligence" of the bot relies on the **k-Nearest Neighbors** algorithm.
* **Vector Space Mapping:** Every question the bot "learns" is mapped as a point in a high-dimensional space.
* **Similarity Search:** When a user types a message, the bot calculates the "distance" between the new input and the existing learned inputs.
* **Threshold Logic:** Your code uses a distance threshold of **0.1**; if the closest match is within this range, the bot considers it a valid match and provides the stored answer.


* **Data Persistence: JSON-based Knowledge Base**
Unlike volatile memory that clears when a program stops, this project uses a **JSON (JavaScript Object Notation)** file for persistent storage. This allows the chatbot to maintain its "memory" across different sessions by loading the `learned_data.json` file into a Python dictionary during startup.
* **Hybrid Retrieval System**
The bot employs a two-tier retrieval strategy:
1. **Keyword Matching:** It first checks if any learned key is explicitly contained within the user's string.
2. **Vector Similarity:** If no direct keyword is found, it falls back to the k-NN model to find the mathematically "nearest" intent.


## 🚀 Features
* **Self-Learning Mechanism:** When the bot encounters an unknown query, it asks the user for the correct response and updates its knowledge base instantly.
* **Intelligent Matching:** Uses `TfidfVectorizer` and `k-Nearest Neighbors` (k-NN) to find the most relevant answers even if the phrasing differs slightly.
* **Admin Dashboard:** A private interface to view chat history, edit learned responses, or delete data.
* **Responsive UI:** Features a modern, dark-themed chat interface with a dynamic background.
* **Persistent Memory:** All learned data is stored in a JSON format, ensuring the bot retains knowledge after a restart.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (TfidfVectorizer, NearestNeighbors)
* **Frontend:** HTML5, CSS3, JavaScript
* **Data Storage:** JSON

## 📋 Prerequisites
Ensure you have Python installed on your system. You will also need the following libraries:
```bash
pip install flask scikit-learn

```

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/PromptPal-Chatbot.git](https://github.com/your-username/PromptPal-Chatbot.git)
cd PromptPal-Chatbot

```


2. **Set up a virtual environment (Optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`

```


3. **Run the application:**
```bash
python app.py

```


4. **Access the app:**
* **Main Chat:** `http://127.0.0.1:5000/`
* **Admin Panel:** `http://127.0.0.1:5000/admin`




## 📂 Project Structure

* `app.py`: The main Flask application containing the logic for NLP and routing.
* `templates/`: Contains HTML files for the Chat UI, Admin Panel, and Learning Page.
* `static/`: Contains the CSS for styling and JavaScript for frontend interactivity.
* `learned_data.json`: The database file where the chatbot's knowledge is stored.

