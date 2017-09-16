import sys, os, traceback, telepot, time, json, random, pprint
import tool, modDatabase, modSearch, modVariables
from modHandle import hande
from modExcute import excut
from msgMain import msgMain
from msgShort import msgShort
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
        self.arg = modVariables.initi()

    def sending(self,mesag=['']):
        lingua = self.arg.get('setti',{}).get('lingua','enMY')
        for wuerd in mesag:
            if len(wuerd) >=4069:
                parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
                for numo in range(0,len(parta)):
                    if numo == 0:
                        sentes = parta[numo] + msgShort(lingua=lingua,tasta='spitpost')
                        self.sender.sendMessage(sentes)
                    elif numo == len(parta) - 1:
                        sentes = msgShort(lingua=lingua,tasta='spitpre') + parta[numo]
                        self.sender.sendMessage(sentes)
                    else:
                        sentes = msgShort(lingua=lingua,tasta='spitpre') + parta[numo]
                        sentes = sentes + msgShort(lingua=lingua,tasta='spitpost')
                        self.sender.sendMessage(sentes)
                    time.sleep(1)
            else:
                self.sender.sendMessage(wuerd)
                time.sleep(1)

    def open(self, initial_msg, seed): # Welcome Region
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        usrdir = 'database/usr/'+str(chat_id)
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        self.arg.update({
            'usrdir' : usrdir,
            'lingua' : lingua,
            'catid' : chat_id,
            'catyp' : chat_type,
            'cotyp' : content_type,
            'primo' : [''],
            'submo' : '',
            'setti' : modDatabase.openSetting(usrdir=usrdir),
            'karat' : modDatabase.openKaratio(usrdir=usrdir),
            'rawdb' : modDatabase.opendb(usrdir=usrdir).get('raw',{}),
            'keydb' : modDatabase.opendb(usrdir=usrdir).get('key',{}),
            'veces' : 0,
        })

        if content_type != 'text':
            self.sending(mesag=[msgMain(lingua=lingua,tasta='error')])
            self.close()
            return

        if "/" in initial_msg['text']:
            resul = excut(msg=initial_msg, arg=self.arg)

            mesut = resul.get('mesut',[])
            self.sending(mesag=mesut)

            arg = self.arg
            self.arg = resul.get('arg',arg)

            cos = resul.get('cos',0)
            if cos == 1:
                self.close()
        elif "/" not in initial_msg["text"]:
            keywo = initial_msg["text"].replace(" ","_")
            self.arg.update({ 'keywo' : keywo })
            self.sending(mesag=[msgMain(lingua=lingua,tasta='home',keyse={'keywo':keywo})])

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        usrdir = 'database/usr/'+str(chat_id)
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        self.arg.update({
            'usrdir' : usrdir,
            'lingua' : lingua,
            'catid' : chat_id,
            'catyp' : chat_type,
            'cotyp' : content_type,
            'veces' : 0,
        })

        if content_type != 'text':
            self.sending(mesag=[msgMain(lingua=lingua,tasta='error')])
            self.close()
            return

        if "/" in msg['text']:
            resul = excut(msg=msg, arg=self.arg)

            mesut = resul.get('mesut',[])
            self.sending(mesag=mesut)

            arg = self.arg
            self.arg = resul.get('arg',arg)

            cos = resul.get('cos',0)
            if cos == 1:
                self.close()

        elif "/" not in msg["text"]:
            resul = hande(msg=msg, arg=self.arg)

            resut = resul.get('resut',[])
            self.sending(mesag=resut)

            arg = self.arg
            self.arg = resul.get('arg',arg)

            cos = resul.get('cos',0)
            if cos == 1:
                self.close()

    def on__idle(self, event): # Timeout Region
        usrdir = 'database/usr/'+str(self.arg.get('catid','admin'))
        lingua = modDatabase.openSetting(usrdir=usrdir).get('lingua','enMY')
        self.sending(mesag=[msgMain(lingua=lingua,tasta='timesout')+msgShort(lingua=lingua,tasta='cof')])
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
