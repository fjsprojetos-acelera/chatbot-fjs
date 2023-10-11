from flask import Flask, render_template, json, jsonify, request
from chatgpt import chatBotRun
import requests
import os
import sys
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        print("teste 1")
        userInput = request.form['user_input']
        print(userInput)
        bot_response = chatBotRun(userInput)
        return jsonify({'response': bot_response})
    except Exception as e:
        print(f'Erro na rota /ask: {e}')
        return jsonify({'error': 'Ocorreu um erro no servidor.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
