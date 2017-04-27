import sys, os, traceback, telepot, time, json, random
import tool, auth, log, mmctool, mmcmsg, mmcdb
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
            "fromm":"","price":"", "karen":"",
            "toooo":"","tpric":"",	"tkare":"",
            "desci":"",

        }
        self._lista = {
            "klass":[""], "shoop":[""],
            "accnt":[""], "karen":[""],
        }
        self._recom = {}
        self._defac = {}
        self._setting = {
            "dinco":"", "dexpe":"",
            "genis":"", "ovede":"",
        }
        self._sf = {
            "d":"datte",
            "n":"namma", "k":"klass", "s":"shoop",
            "f":"fromm", "p":"price",
            "t":"toooo", "r":"tpric",
            "i":"dinco", "e":"dexpe",
            "g":"genis", "o":"ovede",
        }
        self._fs = {
            "datte":"d",
            "namma":"n", "klass":"k", "shoop":"s",
            "fromm":"f", "price":"p",
            "toooo":"t", "tpric":"r",
            "dinco":"i", "dexpe":"e",
            "genis":"g", "ovede":"o",
        }
    #
    def bugpri(self,text): # need migrate to mmctool.py
        print("\n---"+text+"---")
        print("_tem = "+self._keywo)
        print(self._temra)
        print(self._lista)
        print(self._mod)

    def bugpra(self,text,thin): # need migrate to mmctool.py
        print(" --"+text+"-- ")
        print(thin)

    """--------------------------------------------------------
        mmctool.comme(msg)
"""

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        if "/start" in text:
            self.sender.sendMessage(mmcmsg.start())
            if len(self._mod) == 0:
                self.close()
        elif "/help" in text:
            self.sender.sendMessage(mmcmsg.help())
            if len(self._mod) == 0:
                self.close()
        elif "/Setting" in text:
            self.sender.sendMessage(mmcmsg.setting())
        elif "/New" in text:
            if len(self._mod) == 0:
                self._temra["datte"] = tool.date(1,'-')
                self._temra['fromm'] = self._setting['dexpe']
                self._temra['toooo'] = self._setting['ovede']
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                if self._keywo != "":
                    self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))
                self._mod=mmctool.apmod(self._mod,"outo")
        elif "/List" in text:
            self.sender.sendMessage(mmcmsg.lisFilte(self._temra))
            self._mod=mmctool.apmod(self._mod,"list")

        elif "/set_Account" in text:
            if len(self._mod) == 0:
                self._mod=mmctool.apmod(self._mod,"defAcc")
            else:
                if self._mod[-1] != "defAcc":
                    self._mod=mmctool.apmod(self._mod,"defAcc")
            self.sender.sendMessage(mmcmsg.defAccList(self._setting))

        elif len(self._mod) == 0:
            self.sender.sendMessage(mmcmsg.help())
            self.close()

        elif self._mod[-1] == "list":
            if "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.lisFilte(self._temra))
            elif "/Discard" in text:
                self.sender.sendMessage(mmcmsg.lisDiscard())
                self._mod=mmctool.chmod(self._mod)

        elif self._mod[-1] == "outo":

            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                self.bugpri("Discard record")
                self.sender.sendMessage(mmcmsg.outoDiscard())

                self._mod=mmctool.chmod(self._mod)
                self.bugpri("Changed back mode")

            elif "/Save" in text:
                record = mmcdb.addRaw(chat_id,self._temra)
                mmcdb.refesKey(chat_id)
                self.sender.sendMessage(mmcmsg.outoFinis(self._temra))
                self.close()

            elif "/set_as" in text :
                if "/set_as_Date" in text:
                    self._temra["datte"]=self._keywo
                    self._keys='datte'
                elif "/set_as_Item" in text:
                    self._temra["namma"]=self._keywo
                    self._keys='namma'
                elif "/set_as_Category" in text:
                    self._temra["klass"]=self._keywo
                    self._keys='klass'
                elif "/set_as_Seller" in text:
                    self._temra["shoop"]=self._keywo
                    self._keys='shoop'
                elif "/set_as_Price" in text:
                    self._temra["price"]=self._keywo
                    self._keys='price'
                elif "/set_as_Notes" in text:
                    self._temra["desci"]=self._keywo
                    self._keys='desci'

                self.sender.sendMessage(mmcmsg.outo(self._temra))
                if self._keys in ['namma', 'klass', 'shoop', 'price']:
                    self._recom = mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],self._fs,chat_id)
                    if self._recom[1] !="" :
                        self.sender.sendMessage(mmcmsg.outoRecom(self._recom[1],self._keywo))

            elif "/rg" in text :
                for sette in text.split(" "):
                    if "/rgs_" in sette:
                        try:
                            self._temra[self._sf[sette[5]]] = self._recom[2][sette[7:len(sette)]]
                        except KeyError:
                                self.sender.sendMessage("Expected Error : Doesn't Exist or Expired")
                                print("KeyError : Doesn't Exist or Expired")
                    elif "/rg_" in sette:
                        self._temra[self._sf[sette[4]]] = sette[6:len(sette)]
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                self.sender.sendMessage(mmcmsg.outoRecom(self._recom[1],self._keywo))

            elif "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                if self._keywo != "":
                    self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))
        elif self._mod[-1] == "defAcc":

            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                self.bugpri("Discard Account Setting")
                self.sender.sendMessage(mmcmsg.defAccDis())

                self._mod=mmctool.chmod(self._mod)
                self.bugpri("Changed back mode")

            elif "/Save" in text:
                mmcdb.refesSetting(self._setting,chat_id)
                self.sender.sendMessage(mmcmsg.defAccFins(self._setting))
                mmctool.chmod(self._mod)
                self.close()

            elif "/change_" in text:
                keywo = text[8]
                self._defac = {}
                self._defac = mmcdb.listAcc(keywo,chat_id)
                if self._defac[1] !="" :
                    self.sender.sendMessage(mmcmsg.defAccSel(self._defac[1]))

            elif "/ch" in text:
                for sette in text.split(" "):
                    if "/chu_" in sette:
                        try:
                            self._setting[self._sf[sette[5]]] = self._defac[2][sette[7:len(sette)]]
                        except KeyError:
                                self.sender.sendMessage("Expected Error : Doesn't Exist or Expired")
                                print("KeyError : Doesn't Exist or Expired")
                    elif "/ch_" in sette:
                        self._setting[self._sf[sette[4]]] = sette[6:len(sette)]
                self.sender.sendMessage(mmcmsg.defAccList(self._setting))

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.bugpri("Intitial")
        self.bugpra("inti_msg",initial_msg)
        self._mod = []
        self._setting = mmcdb.openSetting(chat_id)
        self.sender.sendMessage(mmcmsg.warn())

        if content_type != 'text':
            self.sender.sendMessage(mmcmsg.error())
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._keywo = initial_msg["text"].replace(" ","_")
            self.sender.sendMessage(mmcmsg.home(self._keywo))

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.bugpri("Received")
        self.bugpra("msg",msg)
        self.sender.sendMessage(mmcmsg.warn())

        if content_type != 'text':
            self.sender.sendMessage(mmcmsg.error())
            self.close()
            return

        if "/" in msg["text"]:
            self.comme(msg)
        else:
            if "/" not in msg["text"]:
                self._keywo = msg["text"].replace(" ","_")

            if len(self._mod) == 0:
                self.sender.sendMessage(mmcmsg.home(self._keywo))
#            elif self._mod[len(self._mod)-1] == "list":
            elif self._mod[-1] == "outo":
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))
            elif self._mod[-1] == "defAcc":
                numme = str(random.choice(range(10,100)))
                self._defac={}
                try:
                    self._keywo.encode('latin-1')
                    self._defac={1:["/ch_","_"+self._keywo],2:[]}
                except UnicodeEncodeError:
                    self._defac={1:["/chu_","_"+numme+" "+self._keywo],2:{numme:self._keywo}}
                self.sender.sendMessage(mmcmsg.defAccSet(self._keywo,self._defac))

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(mmcmsg.timesout())
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
