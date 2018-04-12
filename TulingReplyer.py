from ProcessInterface import ProcessInterface
import itchat
from wxpy import *
import re
import logging


class TulingReplyer(ProcessInterface):
    def __init__(self, api_key, whitelist=[]):
        self.api_key = api_key
        self.whitelist = whitelist
        self.tuling = Tuling(api_key=self.api_key)
        logging.info('TulingReplyer initialized...')


    def process(self, msg):
        if msg.type != 'Text':
            return
        if msg.sender in self.whitelist:
            replyText = self.tuling.reply_text(msg)
            logging.info('{0}, {1} => {2}'.format(msg.sender, msg.text, replyText))
            msg.reply(replyText)
