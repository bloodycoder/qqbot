#!/usr/bin/python
# -*- coding: utf-8 -*-

from qqbot import QQBot
import time
class MyQQBot(QQBot):
    def onPollComplete(self, msgType, from_uin, buddy_uin, message):
    	time.sleep(2)
    	self.send(msgType,from_uin,self.getReturn(message))
    def getReturn(self,message):
    	resent = '这里是树莓派'
    	if('hello' in message):
    		resent = 'hello,how can I help you?'
    	return resent
myqqbot = MyQQBot()
myqqbot.Login(2909501073)
myqqbot.PollForever()
