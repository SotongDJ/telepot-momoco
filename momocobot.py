import sys, os, traceback, telepot, time, json
import tool, auth, log, momoco, mmcmsg, mmcdb
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._tem = ""
        self._mod = []
        self._mem = {
            "namma":"", "klass":"", "shoop":"",
            "datte":"",
            "price":"", "karen":"",
            "fromm":"", "toooo":"",
            "desci":"",
            "tpric":"",	"tkare":"",
        }
        self._lem = {
            "klass":[""], "shoop":[""],
            "accnt":[""], "karen":[""]
        }
        self._rnem = {
            "namma":[], "klass":[], "shoop":[],
            "price":[], "fromm":[],
            "toooo":[], "tpric":[]
        }
        self._sf = {
            "n":"namma", "k":"klass", "s":"shoop",
            "f":"fromm","p":"price",
            "t":"toooo","r":"tpric",
        }
    #
    def bugpri(self,text): # need migrate to momoco.py
        print("\n---"+text+"---")
        print("_tem = "+self._tem)
        print(self._mem)
        print(self._lem)
        print(self._mod)

    def bugpra(self,text,thin): # need migrate to momoco.py
        print(" --"+text+"-- ")
        print(thin)

    """--------------------------------------------------------
        momoco.comme(msg)
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
                self._mem["datte"] = tool.date(1,'-')
                self.sender.sendMessage(mmcmsg.new(self._mem))
                if self._tem != "":
                    self.sender.sendMessage(mmcmsg.newKeywo(self._tem))
                self._mod=momoco.chmod(0,self._mod,"new")
        elif "/List" in text:
            self.sender.sendMessage(mmcmsg.lisFilte(self._mem))
            self._mod=momoco.chmod(0,self._mod,"list")

        elif self._mod[len(self._mod)-1] == "list":
            if "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.lisFilte(self._mem))
            elif "/Discard" in text:
                self.sender.sendMessage(mmcmsg.lisDiscard())
                self._mod=momoco.chmod(1,self._mod,"")

        elif self._mod[len(self._mod)-1] == "new":

            if "/Discard" in text:
                self._tem = ""
                for key in self._mem.keys():
                    self._mem[key]=""

                self.bugpri("Discard record")
                self.sender.sendMessage(mmcmsg.newDiscard())

                self._mod=momoco.chmod(1,self._mod,"")
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
                record["raw"][timta] = self._mem
                record=mmcdb.addkey(timta,self._mem,list(self._rnem.keys()),'key',record)
                self.bugpra("Add Record",record)
                faale = open(tool.path("momoco",chat_id)+"record.json","w")
                json.dump(record,faale)
                faale.close()

                self.sender.sendMessage(mmcmsg.newFinis(self._mem))
                self.close()

            elif "/set_as" in text :
                if "/set_as_Date" in text:
                    self._mem["datte"]=self._tem
                elif "/set_as_Product" in text:
                    self._mem["namma"]=self._tem
                elif "/set_as_Class" in text:
                    self._mem["klass"]=self._tem
                elif "/set_as_Seller" in text:
                    self._mem["shoop"]=self._tem
                elif "/set_as_Price" in text:
                    self._mem["price"]=self._tem
                elif "/set_as_Notes" in text:
                    self._mem["desci"]=self._tem

                self.sender.sendMessage(mmcmsg.new(self._mem))

            elif "/rg_" in text :
                for sette in text.split(" "):
                    if "/rg_" in sette:
                        self._mem[self._sf[sette[4]]] = sette[6:len(sette)]
                self.sender.sendMessage(mmcmsg.new(self._mem))

            elif "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.new(self._mem))
                if self._tem != "":
                    self.sender.sendMessage(mmcmsg.newKeywo(self._tem))


    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.bugpri("New Start")
        self.bugpra("inti_msg",initial_msg)
        self._mod = []
        self.sender.sendMessage(mmcmsg.warn())

        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._tem = initial_msg["text"].replace(" ","_")
            self.sender.sendMessage(mmcmsg.home(self._tem))

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.bugpri("Received")
        self.bugpra("msg",msg)
        self.sender.sendMessage(mmcmsg.warn())

        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        if "/" in msg["text"]:
            self.comme(msg)
        else:
            if "/" not in msg["text"]:
                self._tem = msg["text"].replace(" ","_")

            if len(self._mod) == 0:
                self.sender.sendMessage(mmcmsg.home(self._tem))
#            elif self._mod[len(self._mod)-1] == "list":
            elif self._mod[len(self._mod)-1] == "new":
                self.sender.sendMessage(mmcmsg.new(self._mem))
                self.sender.sendMessage(mmcmsg.newKeywo(self._tem))


    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(mmcmsg.timesout())
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
