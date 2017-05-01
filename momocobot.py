import sys, os, traceback, telepot, time, json, random, pprint
import tool, auth, log, mmctool, mmcdb
from libmsg import mmcMsg, outoMsg, incoMsg, tranMsg, defSettMsg, listMsg
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._keywo = ""
        self._keys = ""
        self._mod = []
        self._temra = {
            "datte":"",
            "namma":"", "klass":"", "shoop":"",
            "fromm":"", "price":"", "karen":"",
            "toooo":"", "tpric":"", "tkare":"",
            "desci":"",
        }
        self._recom = {}
        self._defSett = {}
        self._setting = {
            "dinco":"", "dexpe":"Cash",
            "genis":"Income", "ovede":"Expense",
            "tanfe":"Transfer", "incom":"Income",
            'karen':'',
            'limit':{
                'defSettWarn':0,
                },
        }
        self._sf = {
            "dt":"datte",
            "nm":"namma", "kl":"klass", "sh":"shoop",
            "fr":"fromm", "pr":"price", "kr":"karen",
            "to":"toooo", "tp":"tpric", "tk":"tkare",

            "in":"dinco", "ex":"dexpe",
            "gi":"genis", "oe":"ovede",
            "tf":"tanfe", "ic":"incom",
        }
        self._fs = {
            "datte":"dt",
            "namma":"nm", "klass":"kl", "shoop":"sh",
            "fromm":"fr", "price":"pr", "karen":"kr",
            "toooo":"to", "tpric":"tp", "tkare":"tk",

            "dinco":"in", "dexpe":"ex",
            "genis":"gi", "ovede":"oe",
            "tanfe":"tf", "incom":"ic",
        }
        self._klass = {
            'Acc':['fr','to','in','ex','gi','oe'],
            'Kas':['kl','tf','ic'],
            'Ken':['kr','tk'],
            'Pis':['pr','tp'],
        }
    #
    def printbug(self,text,usrid):
        filla = open(tool.path('log/mmcbot',auth.id())+tool.date(5,'-'),'a')
        print("---"+text+"---")
        filla.write("""
--- pri: """+text+"""---
Time: """+tool.date(2,'-:')+"""
User: """+str(auth.id())+"""
keywo: """+pprint.pformat(self._keywo)+"""
keys: """+pprint.pformat(self._keys)+"""
mod: """+pprint.pformat(self._mod)+"""
temra: """+pprint.pformat(self._temra)+"""
recom: """+pprint.pformat(self._recom)+"""
defSett: """+pprint.pformat(self._defSett)+"""
setting: """+pprint.pformat(self._setting)+"""
--- pri fin ---
""")
        filla.close()

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        if "/start" in text:
            self.sender.sendMessage(mmcMsg.start())
            if len(self._mod) == 0:
                self.close()
        elif "/help" in text:
            self.sender.sendMessage(mmcMsg.help())
            if len(self._mod) == 0:
                self.close()
        elif "/Setting" in text:
            self.sender.sendMessage(mmcMsg.setting(self._setting))
        elif "/exit" in text:
            self.sender.sendMessage("See you next time! Bye!")
            self.close()
        elif "/New" in text:
            if len(self._mod) == 0:
                self._temra["datte"] = tool.date(1,'-')
                self._temra['fromm'] = self._setting['dexpe']
                self._temra['toooo'] = self._setting['ovede']
                self._temra['karen'] = self._setting['karen']
                self._temra['tkare'] = self._setting['karen']
                self.sender.sendMessage(outoMsg.main(self._temra))
                if self._keywo != "":
                    self.sender.sendMessage(outoMsg.keyword(self._keywo))
                self._mod=mmctool.apmod(self._mod,"outo")
        elif "/List" in text:
            self.sender.sendMessage(listMsg.main(self._temra))
            self._mod=mmctool.apmod(self._mod,"list")

        elif "/modify_Setting" in text:
            if len(self._mod) == 0:
                self._mod=mmctool.apmod(self._mod,'defSett')
            else:
                if self._mod[-1] != 'defSett':
                    self._mod=mmctool.apmod(self._mod,'defSett')
            self.sender.sendMessage(defSettMsg.List(self._setting))
            if self._setting['limit']['defSettWarn'] == 0:
                self.sender.sendMessage(defSettMsg.Warn())
                self._setting['limit']['defSettWarn'] = 1
                mmcdb.changeSetting(self._setting,chat_id)

        elif len(self._mod) == 0:
            self.sender.sendMessage(mmcMsg.bored())
            self.close()

        elif self._mod[-1] == "list":
            if "/Whats_Now" in text:
                self.sender.sendMessage(listMsg.main(self._temra))
            elif "/Discard" in text:
                self.sender.sendMessage(listMsg.disca())
                self._mod=mmctool.chmod(self._mod)

        elif self._mod[-1] in ["outo",'inco','tran']:
            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                mmctool.printbug("Discard record\n mod",self._mod,chat_id)
                self.sender.sendMessage(outoMsg.discard())


                self._mod=mmctool.chmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

            elif "/Save" in text:
                record = mmcdb.addRaw(chat_id,self._temra)
                self.sender.sendMessage('Refreshing database...')
                mmcdb.refesdb(chat_id)

                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(outoMsg.finis(self._temra))
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(incoMsg.finis(self._temra))
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(tranMsg.finis(self._temra))
                self.close()

            elif "/set_as" in text :
                if "/set_as_Date" in text:
                    self._temra["datte"]=self._keywo
                    self._keys='datte'
                elif "/set_as_Item" in text:
                    self._temra["namma"]=self._keywo
                    self._keys='namma'
                elif "/set_as_Remind" in text:
                    self._temra["namma"]=self._keywo
                    self._keys='namma'
                elif "/set_as_Category" in text:
                    self._temra["klass"]=self._keywo
                    self._keys='klass'
                elif "/set_as_Seller" in text:
                    self._temra["shoop"]=self._keywo
                    self._keys='shoop'
                elif "/set_as_Source" in text:
                    self._temra["shoop"]=self._keywo
                    self._keys='shoop'
                elif "/set_as_Price" in text:
                    self._temra["price"]=self._keywo
                    self._keys='price'
                elif "/set_as_Notes" in text:
                    self._temra["desci"]=self._keywo
                    self._keys='desci'
                elif "/set_as_Income" in text:
                    self._temra["price"]=self._keywo
                    self._keys='price'
                elif "/set_as_Amount_From" in text:
                    self._temra["price"]=self._keywo
                    self._keys='price'
                elif "/set_as_Amount_To" in text:
                    self._temra["tpric"]=self._keywo
                    self._keys='tpric'

                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(outoMsg.main(self._temra))
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(incoMsg.main(self._temra))
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(tranMsg.main(self._temra))

                if self._keys in ['namma', 'klass', 'shoop', 'price']:
                    self.sender.sendMessage('Refreshing database...')
                    self._recom = mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],self._fs,chat_id)
                    if self._recom[1] !="" :
                        self.sender.sendMessage(outoMsg.recom(self._recom[1],self._keywo))
                    else:
                        self.sender.sendMessage('Give me a word or a number')

            elif "/rg" in text :
                for sette in text.split(" "):
                    if "/rgs_" in sette:
                        try:
                            self._temra[self._sf[sette[5:7]]] = self._recom[2][sette[8:len(sette)]]
                            if self._mod[-1] == 'outo':
                                self.sender.sendMessage(outoMsg.main(self._temra))
                            elif self._mod[-1] == 'inco':
                                self.sender.sendMessage(incoMsg.main(self._temra))
                            elif self._mod[-1] == 'tran':
                                self.sender.sendMessage(tranMsg.main(self._temra))
                            self.sender.sendMessage(outoMsg.recom(self._recom[1],self._keywo))
                        except KeyError:
                                self.sender.sendMessage("Expected Error : Doesn't Exist or Expired")
                                print("KeyError : Doesn't Exist or Expired")

                                if self._mod[-1] == 'outo':
                                    self.sender.sendMessage(outoMsg.main(self._temra))
                                elif self._mod[-1] == 'inco':
                                    self.sender.sendMessage(incoMsg.main(self._temra))
                                elif self._mod[-1] == 'tran':
                                    self.sender.sendMessage(tranMsg.main(self._temra))

                                self.sender.sendMessage('Give me a word or a number')

                    elif "/rg_" in sette:
                        self._temra[self._sf[sette[4:6]]] = sette[7:len(sette)]
                        if self._mod[-1] == 'outo':
                            self.sender.sendMessage(outoMsg.main(self._temra))
                        elif self._mod[-1] == 'inco':
                            self.sender.sendMessage(incoMsg.main(self._temra))
                        elif self._mod[-1] == 'tran':
                            self.sender.sendMessage(tranMsg.main(self._temra))
                        self.sender.sendMessage(outoMsg.recom(self._recom[1],self._keywo))

            elif "/change" in text:
                if "/change_to_" in text:
                    if '/change_to_Income' in text:
                        self._temra['fromm'] = self._setting['genis']
                        self._temra['toooo'] = self._setting['dinco']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['incom']
                        self.sender.sendMessage(incoMsg.main(self._temra))
                        self.sender.sendMessage('Give me a word or a number')
                        self._mod=mmctool.chmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"inco")
                    elif '/change_to_Transfer' in text:
                        self._temra['fromm'] = self._setting['dinco']
                        self._temra['toooo'] = self._setting['dexpe']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['tanfe']
                        self.sender.sendMessage(tranMsg.main(self._temra))
                        self.sender.sendMessage('Give me a word or a number')
                        self._mod=mmctool.chmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"tran")
                    elif '/change_to_Expense' in text:
                        self._temra['fromm'] = self._setting['dexpe']
                        self._temra['toooo'] = self._setting['ovede']
                        self._temra['klass'] = self._setting['']
                        self.sender.sendMessage(outoMsg.main(self._temra))
                        self.sender.sendMessage('Give me a word or a number')
                        self._mod=mmctool.chmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"outo")

                else:
                    self._recom = {}
                    if "/change_Currency_To" in text:
                        keywo = 'tk'
                        self.sender.sendMessage('Refreshing database...')
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(mmcMsg.selection(self._recom[1],'Currency (To)'))
                    elif "/change_Currency" in text:
                        keywo = 'kr'
                        self.sender.sendMessage('Refreshing database...')
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(mmcMsg.selection(self._recom[1],'Currency'))
                    elif "/change_Acc_From" in text:
                        keywo = 'fr'
                        self.sender.sendMessage('Refreshing database...')
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(mmcMsg.selection(self._recom[1],'Account (From)'))
                    elif "/change_Acc_To" in text:
                        keywo = 'to'
                        self.sender.sendMessage('Refreshing database...')
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(mmcMsg.selection(self._recom[1],'Account (To)'))

            elif "/Whats_Now" in text:
                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(outoMsg.main(self._temra))
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(incoMsg.main(self._temra))
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(tranMsg.main(self._temra))

                self.sender.sendMessage('Give me a word or a number')

            elif "/Back" in text:
                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(outoMsg.main(self._temra))
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(incoMsg.main(self._temra))
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(tranMsg.main(self._temra))

                self.sender.sendMessage('Give me a word or a number')

        elif self._mod[-1] == 'defSett':
            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                mmctool.printbug("Discard Account Setting\n mod",self._mod,chat_id)
                self.sender.sendMessage(defSettMsg.discard())

                self._mod=mmctool.chmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

            elif "/Save" in text:
                mmcdb.changeSetting(self._setting,chat_id)
                self.sender.sendMessage(defSettMsg.fins(self._setting))
                mmctool.chmod(self._mod)
                self.close()

            elif "/Explain" in text:
                self.sender.sendMessage(defSettMsg.warn())

            elif "/Back" in text:
                self.sender.sendMessage(defSettMsg.lista(self._setting))

            elif "/Whats_Now" in text:
                self.sender.sendMessage(defSettMsg.lista(self._temra))

            elif "/change_" in text:
                keywo = text[8:10]
                self._defSett = {}
                if keywo in self._klass['Acc']:
                    self.sender.sendMessage('Refreshing database...')
                    self._defSett = mmcdb.listAcc('ch','chu',keywo,chat_id)
                    self.sender.sendMessage(mmcMsg.selection(self._defSett[1],'Account'))
                elif keywo in self._klass['Kas']:
                    self.sender.sendMessage('Refreshing database...')
                    self._defSett = mmcdb.listKas('ch','chu',keywo,chat_id)
                    self.sender.sendMessage(mmcMsg.selection(self._defSett[1],'Category'))
                elif keywo in self._klass['Ken']:
                    self.sender.sendMessage('Refreshing database...')
                    self._defSett = mmcdb.listKen('ch','chu',keywo,chat_id)
                    self.sender.sendMessage(mmcMsg.selection(self._defSett[1],'Currency'))

            elif "/ch" in text:
                for sette in text.split(" "):
                    if "/chu_" in sette:
                        try:
                            self._setting[self._sf[sette[5:7]]] = self._defSett[2][sette[8:len(sette)]]
                        except KeyError:
                                self.sender.sendMessage("Expected Error : Doesn't Exist or Expired")
                                print("KeyError : Doesn't Exist or Expired")
                    elif "/ch_" in sette:
                        self._setting[self._sf[sette[4:6]]] = sette[7:len(sette)]
                self.sender.sendMessage(defSettMsg.lista(self._setting))

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.printbug("Intitial",chat_id)
        mmctool.printbug("inti_msg",initial_msg,chat_id)
        self._mod = []
        self._setting = mmcdb.upgradeSetting(self._setting,chat_id)
        self.sender.sendMessage(mmcMsg.warn())
        self.sender.sendMessage('Refreshing database...')
        mmcdb.refesdb(chat_id)

        if content_type != 'text':
            self.sender.sendMessage(mmcMsg.error())
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._keywo = initial_msg["text"].replace(" ","_")
            self.sender.sendMessage(mmcMsg.home(self._keywo))

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.printbug("Received",chat_id)
        mmctool.printbug("msg",msg,chat_id)
        self.sender.sendMessage(mmcMsg.warn())

        if content_type != 'text':
            self.sender.sendMessage(mmcMsg.error())
            self.close()
            return

        if "/" in msg["text"]:
            self.comme(msg)
        else:
            if "/" not in msg["text"]:
                self._keywo = msg["text"].replace(" ","_")

            if len(self._mod) == 0:
                self.sender.sendMessage(mmcMsg.home(self._keywo))
#            elif self._mod[len(self._mod)-1] == "list":
            elif self._mod[-1] == "outo":
                self.sender.sendMessage(outoMsg.main(self._temra))
                self.sender.sendMessage(outoMsg.keyword(self._keywo))
            elif self._mod[-1] == "inco":
                self.sender.sendMessage(incoMsg.main(self._temra))
                self.sender.sendMessage(incoMsg.keyword(self._keywo))
            elif self._mod[-1] == "tran":
                self.sender.sendMessage(tranMsg.main(self._temra))
                self.sender.sendMessage(tranMsg.keyword(self._keywo))
            elif self._mod[-1] == 'defSett':
                numme = str(random.choice(range(10,100)))
                self._defSett={}
                try:
                    self._keywo.encode('latin-1')
                    self._defSett={1:["/ch_","_"+self._keywo],2:[]}
                except UnicodeEncodeError:
                    self._defSett={1:["/chu_","_"+numme+" "+self._keywo],2:{numme:self._keywo}}
                self.sender.sendMessage(defSettMsg.setup(self._keywo,self._defSett))

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(mmcMsg.timesout())
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
