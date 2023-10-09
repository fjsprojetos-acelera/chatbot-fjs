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

#json.dumps({'user_input' : request.form['user_input']})

@app.route('/ask', methods=['POST'])
def ask():
    url = 'http://127.0.0.1:5000/'
    form_data= {'input': 'user_input'}
    try:
        print("teste 1")
        userInput = requests.post(url, data=form_data)
        print(userInput)
        bot_response = chatBotRun(userInput)
        return jsonify({'response': bot_response})
    except Exception as e:
        print(f'Erro na rota /ask: {e}')
        return jsonify({'error': 'Ocorreu um erro no servidor.'}), 500

if __name__ == '__main__':
    app.run(debug=True)


