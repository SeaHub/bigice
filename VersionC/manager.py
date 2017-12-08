#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Samray <samrayleung@gmail.com>

import datetime
from VersionC.db import query_all_messages
from VersionC.es import Message


def index_all_messages_to_es():
    for result in query_all_messages():
        try:
            message_id = result['id']
            from_user_name = result['from_user_name']
            to_user_name = result['to_user_name']
            content = result['content']
            timestamp = datetime.datetime.fromtimestamp(
                float(result['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
        except TypeError as e:
            # ignore error
            continue
        # create the mappings in elasticsearch
        Message.init()
        # create and save and article
        message = Message(meta={
            'id': message_id}, from_user_name=from_user_name, to_user_name=to_user_name,
            content=content, timestamp=timestamp)
        message.save()

if __name__ == "__main__":
    index_all_messages_to_es()
