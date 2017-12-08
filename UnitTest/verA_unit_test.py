#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Seahub <seahubc@gmail.com>

import unittest
import os
from VersionA import bot_api
from VersionA import train_bot

TRAIN_DB_PATH = 'db.sqlite3'

class TestVersionABot(unittest.TestCase):

    def test_get_response(self):
        self.assertTrue(len(bot_api.get_response('我想你了')))

    def test_train_bot(self):
        train_data = [
            "你好呀，你叫什么名字",
            "我叫大冰，大冰的大，大冰的冰"
        ]

        train_bot.start_training(train_data)
        self.assertTrue(os.path.exists(TRAIN_DB_PATH))
        self.assertTrue(train_bot.get_response(train_data[0]), train_data[1])

if __name__ == '__main__':
    unittest.main()
