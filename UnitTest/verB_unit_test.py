#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# author:Seahub <seahubc@gmail.com>

import unittest
from VersionB import reply
from VersionB import wechat_bot

TESTING_MSG = "HELLO MAN"

class TestVersionBBot(unittest.TestCase):

    def test_reply(self):
        reply_msg = wechat_bot.text_reply({'Text': TESTING_MSG})
        self.assertTrue(reply_msg.find(reply.ABOUT_REPLY))

    def test_get_response(self):
        self.assertTrue(len(wechat_bot.get_response(TESTING_MSG)))

    def test_image_reply(self):
        self.assertTrue(wechat_bot.image_reply(TESTING_MSG) in reply.PICTURE_REPLY)

    def test_recording_reply(self):
        self.assertTrue(wechat_bot.recording_reply(TESTING_MSG) in reply.RECORDING_REPLY)

    def test_attachment_reply(self):
        self.assertTrue(wechat_bot.attachment_reply(TESTING_MSG) in reply.ATTACHMENT_REPLY)

    def test_video_reply(self):
        self.assertTrue(wechat_bot.video_reply(TESTING_MSG) in reply.VIDEO_REPLY)

    def test_map_reply(self):
        self.assertTrue(wechat_bot.map_reply(TESTING_MSG) in reply.MAP_REPLY)

    def test_card_reply(self):
        self.assertTrue(wechat_bot.card_reply(TESTING_MSG) in reply.CARD_REPLY)

    def test_note_reply(self):
        self.assertTrue(wechat_bot.note_reply(TESTING_MSG) in reply.NOTE_REPLY)

    def test_sharing_reply(self):
        self.assertTrue(wechat_bot.sharing_reply(TESTING_MSG) in reply.SHARING_REPLY)

    def test_group_reply(self):
        self.assertTrue(len(wechat_bot.group_reply({'isAt': '1',
                                                    'ActualNickName': 'Seahub',
                                                    'Text': TESTING_MSG})))

    def test_get_text(self):
        self.assertEqual(wechat_bot.get_text({'Text': TESTING_MSG, 'Type': 'Text'}),
                         TESTING_MSG)
        self.assertEqual(wechat_bot.get_text({'Text': TESTING_MSG, 'Type': 'Sharing'}),
                         "发送的其他类型回复")

    def test_xiaoice_answer(self):
        # Method can't be tested when logout
        pass

    def test_add_friend(self):
        # Method can't be tested when logout
        pass

    def test_run(self):
        # self.assertTrue(wechat_bot.run())
        pass

if __name__ == '__main__':
    unittest.main()
