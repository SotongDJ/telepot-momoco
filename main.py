import sys, os, traceback, telepot, time, json, random, pprint
# import tool, auth, log, mmctool, mmcdb, mmcDefauV, mmcAnali, mmcSachi
import tool, modDatabase, modSearch, modVariables
from core import hande, excut
from libmsgMmc import msgMain, mainShort, msgCreo, msgOuto, msgInco, msgTran
from libmsgMmc import msgDefSet, msgList, msgEdit, msgAnali, msgSachi
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
        self.arg = modVariables.inti()

    def sending(self,mesag=['']):
        lingua = self.arg.get('setti',{}).get('lingua','enMY')
        for wuerd in mesag:
            if len(wuerd) >=4069:
                parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
                for numo in range(0,len(parta)):
                    if numo == 0:
                        sentes = parta[numo] + mainShort.woood(lingua=lingua,tasta='spitpost')
                        self.sender.sendMessage(sentes)
                    elif numo == len(parta) - 1:
                        sentes = mainShort.woood(lingua=lingua,tasta='spitpre') + parta[numo]
                        self.sender.sendMessage(sentes)
                    else:
                        sentes = mainShort.woood(lingua=lingua,tasta='spitpre') + parta[numo]
                        sentes = sentes + mainShort.woood(lingua=lingua,tasta='spitpost')
                        self.sender.sendMessage(sentes)
                    time.sleep(1)
            else:
                self.sender.sendMessage(wuerd)
                time.sleep(1)

    def open(self, initial_msg, seed): # Welcome Region
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.printbug("Intitial",chat_id)
        mmctool.printbug("inti_msg",initial_msg,chat_id)
        self._mod = ['']
        self._setting = mmcdb.upgradeSetting(self._setting,chat_id)
        self._karatio = mmcdb.openKaratio()
        self._rawdb = mmcdb.opendb(chat_id)['raw']
        self._keydb = mmcdb.opendb(chat_id)['key']
        self._vez=0
        open(tool.path('log/mmcbot',usrid=auth.id())+tool.date(modde=1)+'.c','a').write('\n')

        if content_type != 'text':
            self.sending(msgMain.error(), modda = 1)
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._keywo = initial_msg["text"].replace(" ","_")
            self.sending(msgMain.home(self._keywo))

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
            self.sending(mesag=msgMain(lingua=lingua,tasta='error'))
            self.close()
            return

        if "/" in msg['text']:
            resul = hande(msg=msg, arg=self.arg)
            mesut = resul.get('mesut',[])
            arg = self.arg
            self.arg = resul.get('arg',arg)
            cos = resul.get('cos',0)
            if cos == 1:
                self.close()
        elif "/" not in msg["text"]:
            keywo = msg["text"].replace(" ","_")
            self.arg.update({ 'keywo' : keywo })
            self.sending(mesag=msgMain(lingua=lingua,tasta='home',keyse={'keywo':keywo}))

    def on__idle(self, event): # Timeout Region
        lingua = self._setting['lingua']
        self.sending(msgMain.timesout()+mainShort.woood(lingua,'cof') , modda = 1 )
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
