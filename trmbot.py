import telepot, time, json, pprint, subprocess
import tool, auth
from telepot.delegate import per_chat_id, create_open, pave_event_space

"""Command list
start - Welcome mmcMsg
help - Command List
temp - check temp
gitpull - update
update - upgrade
ckpy - check status
setting - setting
exit - close conversation
"""

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        for n in ['bot.json','bot.pid','temp.log','git.log','daemon.log']:
            tool.ckpath('database/opt/',n)
    #

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        print('comme[text]:'+text)
        if chat_id != auth.id():
            self.sender.sendMessage("Required more permission")
            self.close()
        elif "/start" in text:
            self.sender.sendMessage("Nothing to Say")
            self.close()
        elif "/help" in text:
            self.sender.sendMessage("Ask my father! (Bot Father isn't my father.)")
            self.close()
        elif "/setting" in text:
            self.sender.sendMessage("What ?!")
            self.close()
        elif "/exit" in text:
            self.sender.sendMessage("See you next time! Bye!")
            self.close()
        elif "/temp" in text:
            subprocess.call(['/opt/vc/bin/vcgencmd', 'measure_temp'], stdout=open('database/opt/temp.log', 'w'))
            self.sender.sendMessage(open("database/opt/temp.log").read())
            self.close()
        elif "/gitpull" in text:
            subprocess.call(['git','pull'],stdout=open("database/opt/git.log",'w'))
            self.sender.sendMessage('\n'.join(open("database/opt/git.log").read().splitlines()))
            self.close()
        
        elif "/update" in text:
            print('/update')
            tool.ckpath('database/opt/','daemon.log')
            subprocess.Popen(['python3', 'daemon.py'],stdout=open('database/opt/daemon.log','w'))
        elif "/mmcd" in text:
            print('/update')
            tool.ckpath('database/opt/','mmcd.log')
            subprocess.Popen(['python3', 'mmcd.py'],stdout=open('database/opt/mmcd.log','w'))
        elif "/kmmc" in text:
            print('/update')
            tool.ckpath('database/opt/','mmcd.log')
            subprocess.Popen(['python3', 'mmckill.py'],stdout=open('database/opt/mmcd.log','w'))

        elif "/ckpy" in text:
            fille = json.load(open("database/opt/bot.json",'r'))
            self.sender.sendMessage(pprint.pformat(fille))
            subprocess.call(['pgrep','-l', 'python'], stdout=open('database/opt/bot.pid', 'w'))
            self.sender.sendMessage('\n'.join(open("database/opt/bot.pid").read().splitlines()))
            self.close()
        else:
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
            self.sender.sendMessage("Pls command me, don't talk to me")

    def on__idle(self, event): # Timeout Region

        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["tsrmdbot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
