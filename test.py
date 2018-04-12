#!/usr/bin/env python3.5
from wxpy import *
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("deepThought")# 用于回复消息的机器人
#chatbot.set_trainer(ChatterBotCorpusTrainer)
#chatbot.train("chatterbot.corpus.chinese")# 使用该库的中文语料库
bot = Bot(cache_path=True)# 用于接入微信的机器人
test_group = bot.groups().search("TestWoodBot")# 进行测试的群

tuling = Tuling(api_key='bb535760f2ee44049193d76df708299d')
yiming_chen = bot.friends().search("Yiming Chen")[0]
junsong = bot.friends().search("Junsong")[0]
jijiji = bot.friends().search('季几集')[0]

@bot.register(junsong)
def replyFriend(msg):
    tuling.do_reply(msg)


@bot.register(yiming_chen)
def replyFriend(msg):
    tuling.do_reply(msg)

@bot.register(jijiji)
def replyFriend(msg):
    tuling.do_reply(msg)
    
#@bot.register(test_group)
#def replyFriend(msg):
#    print(msg)
#    return chatbot.get_response(msg.text).text# 使用机器人进行自动回复

# 堵塞线程，并进入 Python 命令行
embed()
