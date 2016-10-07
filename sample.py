#!/usr/bin/python
# -*- coding: utf-8 -*-

from qqbot import QQBot
import re,urllib2
import time
def read(web):
    s=urllib2.urlopen(web).read()
    return s
class MyQQBot(QQBot):
    def onPollComplete(self, msgType, from_uin, buddy_uin, message):
    	time.sleep(2)
    	self.send(msgType,from_uin,self.getReturn(message))
    def getReturn(self,message):
    	resent = '这里是树莓派'
    	if('hello' in message):
    		resent = 'hello,how can I help you?'
    	elif(message == '-h'):
    		resent = '一键教你玩树莓派聊天机器人。\n输入-h知道全部玩法 \n输入-news知道今天新闻\n输入-e+单词 即可查英文单词\n输入-c+算式 即可进行高精度运算'
    	elif('-news' in message):
    		resent = self.getchina()
    	elif('-e' in message):
    		word = message.split(' ')[1]
    		print word 
    		resent = self.getenglish(word)
    	elif('-c' in message):
    		word = message.split(' ')[1]
    		ans = eval(word)
    		resent = str(ans)
    	return resent
    def getchina(self):
    	myre=re.compile('a href="china[\w|/|_|\.|\d|-]+"\s+target="_blank"\>[\w|\s]+\<')
    	text=read('http://www.chinadaily.com.cn/')
    	A=myre.findall(text)
    	A = ''.join(A)
    	myre=re.compile(r'"\>[\w|-|\s]+\<')
    	A=myre.findall(A)
    	for x in range(len(A)):   
    		A[x]=A[x][2:-1]+'\n'
    	return ''.join(A)
    def getenglish(self,tran):
    	myre=re.compile(r'<span class="family-chinese">.+</span>')
    	text=read('http://www.iciba.com/'+tran)
    	A=myre.findall(text)
    	ans = ''
    	for i in A:
    		ans += i[29:-7]+'\n'
    	return ans
myqqbot = MyQQBot()
myqqbot.Login(2909501073)
myqqbot.PollForever()
