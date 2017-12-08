#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Samray <samrayleung@gmail.com>

import json
import random
import itchat
import requests

from VersionB.reply import (ATTACHMENT_REPLY, CARD_REPLY, MAP_REPLY, NOTE_REPLY,
                            PICTURE_REPLY, RECORDING_REPLY, SHARING_REPLY, VIDEO_REPLY,
                            ABOUT_REPLY)

try:
    with open('tuling.json') as f:
        key = json.loads(f.read())['key']
except:
    # key = ''  # if key is '', get_response will return None
    raise Exception(
        'There is something wrong with tuling.json')


def get_response(msg, storage_class=None, username=None, userid='samray'):
    url = 'http://www.tuling123.com/openapi/api'
    payloads = {
        'key': key,
        'info': msg,
        'userid': userid,
    }

    # noinspection PyBroadException
    try:
        r = requests.post(url, data=json.dumps(payloads)).json()
    except:
        return
    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000):
        return
    if r['code'] == 100000:  # 文本类
        return '\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 200000:  # 链接类
        return '\n'.join([r['text'].replace('<br>', '\n'), r['url']])
    elif r['code'] == 302000:  # 新闻类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']:
            l.append('%s - %s' % (n['article'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 308000:  # 菜谱类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']:
            l.append('%s - %s' % (n['name'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 313000:  # 儿歌类
        return '\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 314000:  # 诗词类
        return '\n'.join([r['text'].replace('<br>', '\n')])

@itchat.msg_register('Text')
def text_reply(msg):
    if u"关于" in msg['Text'] or u"主人" in msg['Text']:
        return ABOUT_REPLY
    else:
        return get_response(msg['Text']) or u'收到：' + msg['Text']

@itchat.msg_register('Picture')
def image_reply(msg):
    return random.choice(PICTURE_REPLY)

@itchat.msg_register('Recording')
def recording_reply(msg):
    return random.choice(RECORDING_REPLY)

@itchat.msg_register('Attachment')
def attachment_reply(msg):
    return random.choice(ATTACHMENT_REPLY)


@itchat.msg_register('Video')
def video_reply(msg):
    return random.choice(VIDEO_REPLY)


@itchat.msg_register('Map')
def map_reply(msg):
    return random.choice(MAP_REPLY)


@itchat.msg_register('Card')
def card_reply(msg):
    return random.choice(CARD_REPLY)


@itchat.msg_register('Note')
def note_reply(msg):
    return random.choice(NOTE_REPLY)


@itchat.msg_register('Sharing')
def sharing_reply(msg):
    return random.choice(SHARING_REPLY)


@itchat.msg_register('Text', isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
                                 get_response(msg['Text']) or u'收到：' + msg['Text'])


def get_text(msg):
    if msg['Type'] == 'Text':
        return msg['Text']
    else:
        return "发送的其他类型回复"


def xiaoice_answer(msg):
    xb = itchat.search_mps(name='小冰')[0]
    quest = get_text(msg)
    if msg['Type'] == 'Picture':
        msg['Text'](msg['FileName'])
        itchat.send_image(msg['FileName'], xb['UserName'])
    else:
        itchat.send_msg(quest, xb['UserName'])


@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'Nice to meet you', msg['RecommendInfo']['UserName'])

def run():
    itchat.auto_login(True, enableCmdQR=2)
    itchat.run()
    return True

if __name__ == "__main__":
    run()
