# -*- coding: utf-8 -*-
from HelpResponder import HelpResponder
from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from TulingReplyer import TulingReplyer
import logging
from sys import argv, exit


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

isDebug = True

chatbot = ChatBot("deepThought")# 用于回复消息的机器人
chatbot.set_trainer(ChatterBotCorpusTrainer)
#chatbot.train("chatterbot.corpus.chinese")# 使用该库的中文语料库
bot = Bot(cache_path=True)# 用于接入微信的机器人
test_group = bot.groups().search("TestWoodBot")# 进行测试的群

api_key='bb535760f2ee44049193d76df708299d'
def getFriendByNickName(nick_name):
    f = bot.friends().search(nick_name)
    if f is not Null:
        return f[0]
    else:
        return ''

yimingchen = getFriendByNickName('Yiming Chen')
junsong = getFriendByNickName('Junsong')
jijiji = getFriendByNickName('季几集')
woodlovepecker = getFriendByNickName('WoodLovePecker')

#yiming_chen = bot.friends().search("Yiming Chen")[0]
#junsong = bot.friends().search("Junsong")[0]
#jijiji = bot.friends().search('季几集')[0]
#woodLovePecker = bot.friends().search('WoodLovePecker')[0]

whitelist = [yiming_chen, junsong, jijiji, woodlovepecker]


plugins = [HelpResponder(), TulingReplyer(api_key=api_key, whitelist=whitelist)]

@bot.register(chats=whitelist, msg_types=TEXT)
def replyFriend(msg):
    if isDebug:
        logging.info(msg)
    for plugin in plugins:
        try:
            plugin.process(msg)
        except Exception as e:
            logging.error(e)



# @bot.register(yiming_chen)
# def replyFriend(msg):
#     tuling.do_reply(msg)
#
# @bot.register(jijiji)
# def replyFriend(msg):
#     tuling.do_reply(msg)

#@bot.register(test_group)
#def replyFriend(msg):
#    print(msg)
#    return chatbot.get_response(msg.text).text# 使用机器人进行自动回复

# 堵塞线程，并进入 Python 命令行
embed()

