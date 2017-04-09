import sys, os, traceback, telepot, time, tool, auth, log
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._tem = {"temp":"", "text":"", "numo":"",}
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
            self.sender.sendMessage("""This chatbot is under constructing...""")

    def _msg(self,msg,statu):
        ma="Status:\n"+statu+"\nInput:\n"+msg["text"]+"\n-------------------------"
        mb="\nPending: "+self._tem[self._tem["temp"]]
        mc="\n/Product : "+self._mem["namma"]+"\n/Class : "+self._mem["klass"]+"\n/Seller : "+self._mem["shoop"]
        md="\n/Date : "+self._mem["datte"]
        me="\n/Price : "+self._mem["price"]
        mf="\n/Currency : "+"\nSpent from: (what acc.)"+"\nTarget account: (If have)"# from self._setting
        mg="\n-------------------------"+"\nTotal spent today:"
        mh="\n-------------------------"+"\n/discard to discard"+"\n/add to add new account"+"\n/setting to change the setting"
        return ma+mb+mc+md+me+mf+mg+mh

    def _comme(self,text):
        print("")

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        print("-------")
        print(initial_msg)
        print(self._tem)
        print(self._mem)
        self._mem["mode"] = "inti"
        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return
        self._mem["datte"] = str(time.localtime(time.time())[0])+"-"+str(time.localtime(time.time())[1])+"-"+str(time.localtime(time.time())[2])
        try:
            numo = int(initial_msg["text"])
            self._tem["numo"] = initial_msg["text"]
            self._tem["temp"] = "numo"
            self.sender.sendMessage(self._msg(initial_msg,"Creating new record"))
        except ValueError:
            if "/" in initial_msg["text"]:
                self._comme(initial_msg["text"])
                self.close()
            else:
                self._tem["nama"] = initial_msg["text"]
                self._tem["temp"] = "nama"
                self.sender.sendMessage(self._msg(initial_msg,"Creating new record"))
        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        print("-------")
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
            self._tem["numo"] = msg["text"]
            self._tem["temp"] = "numo"
            self.sender.sendMessage(self._msg(msg,"Creating on the way"))
        except ValueError:
            if "/" in msg["text"]:
                self._comme(msg["text"])
                self.close()
            else:
                self._tem["nama"] = msg["text"]
                self._tem["temp"] = "nama"
                self.sender.sendMessage(self._msg(msg,"Creating on the way"))

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage("Time's out")
        self.close()


TOKEN = sys.argv[1]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
