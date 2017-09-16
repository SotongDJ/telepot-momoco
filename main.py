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
        self.printbug("Received",chat_id)
        mmctool.printbug("msg",msg,chat_id)
        lingua = self._setting['lingua']

        if content_type != 'text':
            self.sending(msgMain.error(), modda = 1)
            self.close()
            return

        if msg["text"][0] == '/':
            self.comme(msg)
        else:
            self._keywo = msg["text"].replace("/","")

            if self._mod[-1] == '':
                self.sending(msgMain.home(self._keywo))

            elif self._mod[-1] == "list":
                if self._sumo == 'sachi':
                    self.sending(msgSachi.listKeywo(lingua,self._keywo))
                else:
                    self.sending(mainShort.woood(lingua,'emptysachi'))

            elif self._mod[-1] == "edit":
                tasEdit = msgEdit.keyword(self._keywo)
                self.sending(tasEdit)

            elif self._mod[-1] == 'statics':
                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioKeywo(lingua,self._keywo))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenKeywo(lingua,self._keywo))
                elif self._statics['mode'] == 'akaun':
                    self.sending(msgAnali.akaunKeywo(lingua,self._keywo))

            elif self._mod[-1] == "creo":
                if self._sumo == 'outo':
                    tasOut= msgCreo.keyword(self._keywo)
                    self.sending(tasOut)
                elif self._sumo == 'inco':
                    tasInco = msgInco.keyword(self._keywo)
                    self.sending(tasInco)
                elif self._sumo == 'tran':
                    tasTran = msgTran.keyword(self._keywo)
                    self.sending(tasTran)

            elif self._mod[-1] == 'defSett':
                numme = str(random.choice(range(10,100)))
                self._defSett={}
                try:
                    self._keywo.encode('latin-1')
                    self._defSett={1:["/ch_","_"+self._keywo],2:[]}
                except UnicodeEncodeError:
                    self._defSett={1:["/chu_","_"+numme+" "+self._keywo],2:{numme:self._keywo}}
                self.sending(msgDefSet.setup(self._keywo,self._defSett))

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
