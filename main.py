import sys, os, traceback, telepot, time, json, random, pprint

from core import tool
from core import modDatabase

import modSearch, modArgona, auth

from modHandle import Hande
from modExcute import Excut
from msgMain import MsgMain
from msgShort import MsgShort
from telepot.delegate import per_chat_id, create_open, pave_event_space

"""Command list
help - Show command list
whats_now - Show current unsaved work
new - Create new record
list - Show prevous record
statics - View statistics card
start - Welcome and Introduction
setting - View setting card
exit - Close conversation
"""

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.argo = modArgona.Argo()

    def sending(self,mesag=['']):
        lingua = self.argo.setti.get('lingua','enMY')
        msgShort = MsgShort(lingua)
        for wuerd in mesag:
            if len(wuerd) >=4069:
                parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
                for numo in range(0,len(parta)):
                    if numo == 0:
                        sentes = parta[numo] + msgShort.spitpost
                        self.sender.sendMessage(sentes)
                    elif numo == len(parta) - 1:
                        sentes = msgShort.spitpre + parta[numo]
                        self.sender.sendMessage(sentes)
                    else:
                        sentes = msgShort.spitpre + parta[numo]
                        sentes = sentes + msgShort.spitpost
                        self.sender.sendMessage(sentes)
                    time.sleep(1)
            else:
                self.sender.sendMessage(wuerd)
                time.sleep(1)

    def open(self, initial_msg, seed): # Welcome Region
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        usrdir = 'database/usr/'+str(chat_id)
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        defal = modArgona.Argo()
        msgMain = MsgMain(lingua)

        self.argo.usrdir = usrdir
        self.argo.lingua = lingua
        chatdata = self.argo.database.get('chat',{})
        chatdata.update({ 'chatid' : chat_id })
        chatdata.update({ 'chattype' : chat_type })
        chatdata.update({ 'content_type' : content_type })
        self.argo.database.update({ 'chat' : chatdata })
        self.argo.database.update({ 'mode' : { 0 : '' } })
        self.argo.setti = modDatabase.openSetting(usrdir=usrdir)
        self.argo.veces = 0

        if content_type != 'text':
            self.sending(mesag=[msgMain.error])
            self.close()
            return

        # if "/" in initial_msg['text']:
        if initial_msg['text'][0] == "/":
            resul = Excut(initial_msg['text'],self.argo)

            self.sending(mesag=resul.mesut)
            self.argo = resul.argo
            if resul.cos == 1:
                self.close()

        # elif "/" not in initial_msg["text"]:
        else:
            keywo = initial_msg["text"]
            self.argo.keywo = keywo
            self.sending(mesag=[msgMain.home({'keywo':keywo})])

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        usrdir = 'database/usr/'+str(chat_id)
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        msgMain = MsgMain(lingua)
        self.argo.usrdir = usrdir
        self.argo.lingua = lingua
        chatdata = self.argo.database.get('chat',{})
        chatdata.update({ 'chatid' : chat_id })
        chatdata.update({ 'chattype' : chat_type })
        chatdata.update({ 'content_type' : content_type })
        self.argo.database.update({ 'chat' : chatdata })
        self.argo.veces = 0

        if content_type != 'text':
            self.sending(mesag=[msgMain.error])
            self.close()
            return

        # if "/" in msg['text']:
        if msg['text'][0] == "/":
            resul = Excut(msg['text'],self.argo)

            self.sending(mesag=resul.mesut)
            self.argo = resul.argo
            if resul.cos == 1:
                self.close()

        # elif "/" not in msg["text"]:
        else:
            resul = Hande(msg['text'],self.argo)

            self.sending(mesag=resul.resut)
            self.argo = resul.argo
            if resul.cos == 1:
                self.close()
            elif resul.ekgu == 1:
                resul = Excut(msg['text'],self.argo)

                self.sending(mesag=resul.mesut)
                self.argo = resul.argo
                if resul.cos == 1:
                    self.close()

    def on__idle(self, event): # Timeout Region
        usrdir = 'database/usr/'+str(self.argo.database.get('chat',{}).get('chatid',auth.id()))
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        self.sending(mesag=[msgMain.timesout + msgShort.cof])
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
