import sys, os, traceback, telepot, time, json, tool, auth, log, momoco, mmcmsg
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._tem = ""
        self._mod = []
        self._mem = {
            "namma":"", "klass":"", "shoop":"",
            "datte":"", "price":"",
            "karen":"",
            "fromm":"", "toooo":"",
        }
        self._lem = {
            "klass":[""], "shoop":[""],
            "accnt":[""], "karen":[""]
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
            if self._mod[len(self._mod)-1] == "":
                self.close()
        elif "/help" in text:
            self.sender.sendMessage(mmcmsg.help())
            if self._mod[len(self._mod)-1] == "":
                self.close()
        elif "/Setting" in text:
            self.sender.sendMessage(mmcmsg.setting())
        elif "/New" in text:
            if self._mod[len(self._mod)-1] == "":
                self.sender.sendMessage(mmcmsg.newStart(self._mem,self._tem))
                self._mod=momoco.chmod(0,self._mod,"")
        elif "/List" in text:
            self.sender.sendMessage(mmcmsg.lisFilte(self._mem))
            self._mod=momoco.chmod(0,self._mod,"")

        elif self._mod[len(self._mod)-1] == "list":
            if "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.lisFilte(self._mem))
            elif "/Discard" in text:
                self.sender.sendMessage(mmcmsg.lisDiscard())
                self._mod=momoco.chmod(1,self._mod,"")

        elif self._mod[len(self._mod)-1] == "new":

            if "/Whats_Now" in text:
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))
            elif "/set_as_Date" in text:
                dicto["datte"]=self._tem
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))
            elif "/set_as_Product" in text:
                dicto["namma"]=self._tem
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))
            elif "/set_as_Class" in text:
                dicto["klass"]=self._tem
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))
            elif "/set_as_Seller" in text:
                dicto["shoop"]=self._tem
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))
            elif "/set_as_Price" in text:
                dicto["price"]=self._tem
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))

            elif "/Discard" in text:
                self._tem = ""
                for key in self._mem.keys():
                    self._mem[key]=""

                self.bugpri("Discard recod")
                self.sender.sendMessage(mmcmsg.newDiscard())

                self._mod=momoco.chmod(mode_num,self._mod,mode_text)
                self.bugpri("Changed back mode")

            elif "/Save" in text:
                recod={}

                try:
                    faale = open(tool.path("momoco",chat_id)+self._mem["datte"]+".json","r")
                    recod = json.load(faale)
                    self.bugpra("Old Record",recod)
                    faale.close()
                except FileNotFoundError:
                    record = {}

                #try:
                recod[tool.date(4)] = self._mem
                self.bugpra("Add Record",recod)
                faale = open(tool.path("momoco",chat_id)+self._mem["datte"]+".json","w")
                json.dump(recod,faale)
                faale.close()

                self.sender.sendMessage(mmcmsg.newConti(self._mem))
                self.close()

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.bugpri("New Start")
        self.bugpra("inti_msg",initial_msg)
        self._mod = []
        self._tem = initial_msg["text"]

        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        self._mem["datte"] = tool.date(1)

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            self.sender.sendMessage(mmcmsg.home(self._tem))

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.bugpri("Received")
        self.bugpra("msg",msg)
        self._tem = msg["text"]

        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        if "/" in msg["text"]:
            self.comme(msg)
        else:
            if self._mod[len(self._mod)-1] == "":
                self._tem = msg["text"]
                self.sender.sendMessage(mmcmsg.home(self._tem))
#            elif self._mod[len(self._mod)-1] == "list":
            elif self._mod[len(self._mod)-1] == "new":
                self._tem = msg["text"]
                self.sender.sendMessage(mmcmsg.newConti(self._mem,self._tem))


    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(mmcmsg.timesout())
        self.close()


TOKEN = sys.argv[1]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
