document.addEventListener('DOMContentLoaded', function () {
    const chatLog = document.getElementById('chat-log');
    const userInputForm = document.getElementById('user-input-form');
    const userInput = document.getElementById('user-input');

    userInputForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const userMessage = userInput.value;
        console.log(userMessage)
        if (userMessage.trim() !== '') {
            appendUserMessage(userMessage);
            getUserResponse(userMessage);
            userInput.value = '';
        }
    });

    function appendUserMessage(message) {
        chatLog.innerHTML += `<div class="user-message title-user">${message}</div>`;        
    }

    function getUserResponse(userMessage) {
        const json = JSON.stringify({ user_input: userMessage })
        console.log(json)
        fetch('http://127.0.0.1:5000/ask', {
            method: 'POST',
            body: json,
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            appendBotMessage(botResponse);
        })
        .catch(error => {
            console.error('Erro ao obter resposta do servidor:', error);
        });
    }

    function appendBotMessage(message) {
        chatLog.innerHTML += `<div class="bot-message">${message}</div>`;
    }
});
