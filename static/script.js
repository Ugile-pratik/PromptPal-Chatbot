const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const message = userInput.value;
        if (message.trim()) {
            addMessage('User: ' + message);
            sendMessageToBot(message);
            userInput.value = '';
        }
    }
});

function addMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}

function sendMessageToBot(message) {
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        addMessage('Chatbot: ' + data.response);
        if (data.response === "I don't know the answer. Please provide the correct answer.") {
            learnAnswer(message);
        }
    });
}

function learnAnswer(userInput) {
    const correctAnswer = prompt("Please provide the correct answer:");
    if (correctAnswer) {
        fetch('/learn', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput, correct_answer: correctAnswer })
        })
        .then(response => response.json())
        .then(data => {
            addMessage('Chatbot: I have learned the correct answer!');
        });
    }
}
