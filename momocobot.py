import sys, os, traceback, telepot, tool, auth, log
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._tem = {"temp":"", "text":"", "numo":0,}
        self._mem = {
            "mode":"",
            "namma":"",
            "klass":"",
            "shoop":"",
            "emout":0,
            "karen":"",
            "fromm":"",
            "toooo":"",
        }
    #
    def _ask(self):
        self.sender.sendMessage("""Welcome!
This is Money Money Come Chatbot.
It can help you to trace your money flow more easily (Sure?)
Reply /help to learn more~""")

    #def _msg(self):

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        print(initial_msg)
        print(self._tem)
        print(self._mem)
        self._mem["mode"] = "inti"
        if content_type != 'text':
            self.sender.sendMessage("Status:\n    Received wrong message\nInput:\n    Undetactable content type\n")
            self.close()
            return

        try:
            numo = int(initial_msg["text"])
            self._tem["numo"] = numo
            self._tem["temp"] = "numo"
            self.sender.sendMessage(
                "Status:\n    Creating new record\nInput:\n    "+
                initial_msg["text"]+
                "\n-------------------------\nPending:"+initial_msg["text"]+
                "/Product Name:\n/Class :\n/Seller :\n/Price :\n/Currency :\n"+
                ""+ # Currency from self._setting
                "Spent from:\n"+
                ""+ # Source from self._setting
                "Destination: (If have)"+
                "" # Deposit from self._setting
            )
        except ValueError:
            if "/" in initial_msg["text"]:
                if "/start" in initial_msg["text"]:
                    self._ask()
                    self.close()
            else:
                self._tem["nama"] = initial_msg["text"]
                self._tem["temp"] = "nama"
                self.sender.sendMessage(
                    "Status:\n    Creating new record\nInput:\n    "+
                    initial_msg["text"]+
                    "\n-------------------------\nPending:\n    "+initial_msg["text"]+
                    "/Product name:\n/Class :\n/Seller :\n/Price :\n/Currency :\n"+
                    ""+ # Currency from self._setting
                    "Spent from: (what acc.)\n"+
                    ""+ # Source from self._setting
                    "Target account: (If have)\n"+
                    ""+
                    "\n-------------------------\n"+
                    ""+
                    "\n-------------------------\n/discard to discard\n/add to add new account\n/setting" # Deposit from self._setting
                )
        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        print("-------")
        print(msg)
        print(self._tem)
        print(self._mem)
        if content_type != 'text':
            self.sender.sendMessage('Give me a number, please.')
            return

        try:
           guess = int(msg['text'])
        except ValueError:
            self.sender.sendMessage('Give me a number, please.')
            return

        # check the guess against the answer ...
        if guess != self._answer:
            # give a descriptive hint
            hint = self._hint(self._answer, guess)
            self.sender.sendMessage(hint)
        else:
            self.sender.sendMessage('Correct!')
            self.close()

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage("Time's out")
        self.close()


TOKEN = sys.argv[1]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
