#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Samray <samrayleung@gmail.com>

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, jsonify, request

deep_thought = ChatBot("deepThought")
deep_thought.set_trainer(ChatterBotCorpusTrainer)
deep_thought.train("chatterbot.corpus.chinese")  # 使用中文语料库训练它
app = Flask(__name__)


@app.route("/chatbot")
def get_response():
    user_input = request.args.get('user_input')
    response = {'reply': get_response(user_input)}
    return jsonify(response)

def get_response(request_data):
    return deep_thought.get_response(request_data).text

if __name__ == "__main__":
    app.run()
