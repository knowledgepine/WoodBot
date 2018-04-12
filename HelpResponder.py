# -*- coding: utf-8 -*-
from itchat.content import *
from ProcessInterface import ProcessInterface
import itchat
import wxpy
import re
import logging

class HelpResponder(ProcessInterface):
    dict = {'^/help$': """Instructions：
                /activity: Check the activity of this group
                /tagcloud: See the cloud tag of this group
                /mytag: See your cloud tag
                /doutu: Enter doutu mode. Last for five minutes."""}

    def __init__(self, subdict={}, blacklist=[], whitelist=[]):
        self.dict = {**self.dict, **subdict}
        self.blacklist = blacklist
        self.whitelist = whitelist
        logging.info('HelpResponder initialized...')


    def process(self, msg):
        if msg.type != 'Text':
            return
        if any([ re.search(x, msg.sender) is not None for x in self.blacklist]):
            return
        for k in self.dict:
            if re.search(k, msg.text):
                v = self.dict[k]
                logging.info('help: {0} => {1}'.format(msg.text, v))
                msg.reply(v)

