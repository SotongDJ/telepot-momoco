import sys, os, traceback, telepot, time, json, tool, auth, log
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._tem = ""
        self._mem = {
            "mode":"",
            "namma":"",
            "klass":"",
            "shoop":"",
            "datte":"",
            "price":"",
            "karen":"",
            "fromm":"",
            "toooo":"",
        }
    #
    def _ask(self,text):
        if "/start" in text:
            self.sender.sendMessage("""Welcome!
This is Money Money Come Chatbot.
It can help you to trace your money flow more easily (Sure?)
Reply /help to learn more~""")
        elif "/help" in text:
            self.sender.sendMessage("""This chatbot is under constructing...
Reply:
    /setting to change the setting
""")

    def _msg(self,msg,statu):
        ma="Status: "+statu+"\nInput: "+msg["text"]
        mb="\nPending: "+self._tem+"\n-------------------------"
        mc="\n/Product : "+self._mem["namma"]+"\n/Class : "+self._mem["klass"]+"\n/Seller : "+self._mem["shoop"]
        md="\n/Date : "+self._mem["datte"]+" (yyyy-mm-dd)"
        me="\n/Price : "+self._mem["price"]
        mf="\n/Currency : "+"\nSpent from: (which /Account )\n    /Choose_In_Acc\nTarget account: (If have)\n    /Choose_Out_Acc"# from self._setting
        mg="\n-------------------------"+"\nTotal spent today:"
        mh="\n-------------------------"+"\n/Save to save the record\n/Discard to discard"+"\n/help for more command"
        return ma+mb+mc+md+me+mf+mg+mh

    def _comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        asske=["/start", "/help"]
        trans={"/Product":"namma", "/Class":"klass", "/Seller":"shoop", "/Price":"price"}
        #comme=["/Date","/Currency","/Account","/setting", "/discard", "/Save"]
        text=msg['text']
        for key in asske:
            if key in text:
                self._ask(text)
                self.close()
        for key in trans.keys():
            if key in text:
                if self._tem == "":
                    self.sender.sendMessage(self._msg(msg,"Error: empty value"))
                else:
                    self._mem[trans[key]]=self._tem
                    self._tem=""
                    self.sender.sendMessage(self._msg(msg,"Assign value from "+key))
        if "/Discard" in text:
            self._tem = ""
            for key in self._mem.keys():
                self._mem[key]=""
            self.sender.sendMessage("Status:\n    Discard changes, record removed\nInput:\n"+msg['text'])
        if "/Save" in text:
            recod={}

            try:
                faale = open(tool.path("momoco",chat_id)+self._mem["datte"]+".json","r")
                recod = json.load(faale)
                print("---Old Record---")
                print(recod)
                faale.close()
            except FileNotFoundError:
                record = {}

            recod[tool.date(4)] = self._mem
            print("---Add Record---")
            print(recod)
            faale = open(tool.path("momoco",chat_id)+self._mem["datte"]+".json","w")
            json.dump(recod,faale)
            faale.close()
            self.sender.sendMessage(self._msg(msg,"New record saved"))
            self.close()
    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        print("---New---")
        print(initial_msg)
        print(self._tem)
        print(self._mem)
        self._mem["mode"] = "inti"
        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return
        self._mem["datte"] = tool.date(1)
        try:
            numo = int(initial_msg["text"])
            self._tem = initial_msg["text"]
            self.sender.sendMessage(self._msg(initial_msg,"Creating new record"))
        except ValueError:
            if "/" in initial_msg["text"]:
                self._comme(initial_msg)
            else:
                self._tem = initial_msg["text"]
                self.sender.sendMessage(self._msg(initial_msg,"Creating new record"))
        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        print("---Received---")
        print(msg)
        print(self._tem)
        print(self._mem)
        self._mem["mode"] = "inti"
        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        try:
            numo = int(msg["text"])
            self._tem = msg["text"]
            self.sender.sendMessage(self._msg(msg,"Receive word"))
        except ValueError:
            if "/" in msg["text"]:
                self._comme(msg)
            else:
                self._tem = msg["text"]
                self.sender.sendMessage(self._msg(msg,"Receive word"))

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage("Time's out")
        self.close()


TOKEN = sys.argv[1]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
