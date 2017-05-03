import telepot, time, json, pprint, subprocess
import tool, auth, daemon
from telepot.delegate import per_chat_id, create_open, pave_event_space

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    #

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        if chat_id != auth.id():
            self.sender.sendMessage("Required more permission")
            self.close()
        elif "/start" in text:
            self.sender.sendMessage("Nothing to Say")
            if len(self._mod) == 0:
                self.close()
        elif "/help" in text:
            self.sender.sendMessage("Ask my father! (Bot Father isn't my father.)")
            if len(self._mod) == 0:
                self.close()
        elif "/Setting" in text:
            self.sender.sendMessage("What ?!")
        elif "/exit" in text:
            self.sender.sendMessage("See you next time! Bye!")
            self.close()
        elif "/temp" in text:
            subprocess.call(['/opt/vc/bin/vcgencmd', 'measure_temp'], stdout=open('database/temp', 'w'))
            self.sender.sendMessage(open("database/temp").read())
        elif "/update" in text:
            daemon.update('momocobot')
        elif "/ckpy" in text:
            fille = json.load(open("database/opt/bot.json",'r'))
            self.sender.sendMessage(pprint.pformat(fille)).read())
            self.sender.sendMessage(open("database/opt/bot.pid",'r'))

        elif len(self._mod) == 0:
            self.sender.sendMessage("I don't know that you said")
            self.close()

    def open(self, initial_msg, seed): # Welcome Region
        # self.sender.sendMessage('Guess my number')
        content_type, chat_type, chat_id = telepot.glance(initial_msg)

        if content_type != 'text':
            self.sender.sendMessage("Can't read !!")
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if len(self._mod) == 0:
                self.sender.sendMessage("Pls command me, don't talk to me")

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != 'text':
            self.sender.sendMessage("Can't read !!")
            self.close()
            return

        if "/" in msg["text"]:
            self.comme(msg)
        else:
            if len(self._mod) == 0:
                self.sender.sendMessage("Pls command me, don't talk to me")

    def on__idle(self, event): # Timeout Region

        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["tsrmdbot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
