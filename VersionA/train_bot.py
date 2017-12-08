#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Samray <samrayleung@gmail.com>

from __future__ import unicode_literals

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

deep_thought = ChatBot("Training demo")
deep_thought.set_trainer(ListTrainer)

def start_training(train_data):
    if isinstance(train_data, list):
        deep_thought.train(train_data)
    else:
        raise TypeError("Train_data need to be 'list' type")

def get_response(request_data):
    return deep_thought.get_response(request_data).text

