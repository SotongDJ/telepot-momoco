import sys, os, traceback, telepot, time, json
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
        self._recom = {
            "namma":[], "klass":[], "shoop":[],
            "fromm":[], "price":[],
            "toooo":[], "tpric":[],
        }
        self._sf = {
            "d":"datte",
            "n":"namma", "k":"klass", "s":"shoop",
            "f":"fromm", "p":"price",
            "t":"toooo", "r":"tpric",
        }
        self._fs = {
            "datte":"d",
            "namma":"n", "klass":"k", "shoop":"s",
            "fromm":"f", "price":"p",
            "toooo":"t", "tpric":"r",
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
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                if self._keywo != "":
                    self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))
                self._mod=mmctool.chmod(0,self._mod,"outo")
        elif "/List" in text:
            self.sender.sendMessage(mmcmsg.lisFilte(self._temra))
            self._mod=mmctool.chmod(0,self._mod,"list")

        elif self._mod[len(self._mod)-1] == "list":
            if "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.lisFilte(self._temra))
            elif "/Discard" in text:
                self.sender.sendMessage(mmcmsg.lisDiscard())
                self._mod=mmctool.chmod(1,self._mod,"")

        elif self._mod[len(self._mod)-1] == "outo":

            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                self.bugpri("Discard record")
                self.sender.sendMessage(mmcmsg.outoDiscard())

                self._mod=mmctool.chmod(1,self._mod,"")
                self.bugpri("Changed back mode")

            elif "/Save" in text:
                record = {
                    'raw':{},
                    'key':{},
                    'rank':{}
                    }

                try:
                    faale = open(tool.path("momoco",chat_id)+"record.json","r")
                    record = json.load(faale)
                    self.bugpra("Old Record",record)
                    faale.close()
                except FileNotFoundError:
                    record = {
                        'raw':{},
                        'key':{},
                        'rank':{}
                        }

                #try:
                timta = tool.date(3,'0000')
                record["raw"][timta] = self._temra
                record=mmcdb.addKey(timta,self._temra,'key',record)
                self.bugpra("Add Record",record)
                faale = open(tool.path("momoco",chat_id)+"record.json","w")
                json.dump(record,faale)
                faale.close()

                self.sender.sendMessage(mmcmsg.outoFinis(self._temra))
                self.close()

            elif "/set_as" in text :
                if "/set_as_Date" in text:
                    self._temra["datte"]=self._keywo
                elif "/set_as_Product" in text:
                    self._temra["namma"]=self._keywo
                elif "/set_as_Class" in text:
                    self._temra["klass"]=self._keywo
                elif "/set_as_Seller" in text:
                    self._temra["shoop"]=self._keywo
                elif "/set_as_Price" in text:
                    self._temra["price"]=self._keywo
                elif "/set_as_Notes" in text:
                    self._temra["desci"]=self._keywo

                self.sender.sendMessage(mmcmsg.outo(self._temra))

            elif "/rg_" in text :
                for sette in text.split(" "):
                    if "/rg_" in sette:
                        self._temra[self._sf[sette[4]]] = sette[6:len(sette)]
                self.sender.sendMessage(mmcmsg.outo(self._temra))

            elif "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                if self._keywo != "":
                    self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))


    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.bugpri("outo Start")
        self.bugpra("inti_msg",initial_msg)
        self._mod = []
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
            elif self._mod[len(self._mod)-1] == "outo":
                self.sender.sendMessage(mmcmsg.outo(self._temra))
                self.sender.sendMessage(mmcmsg.outoKeywo(self._keywo))


    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(mmcmsg.timesout())
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
