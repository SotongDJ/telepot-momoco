import sys
import time
import pprint
import telepot

def handle(msg):
    print(msg)
    # Do your stuff here ...
    #postmsg=msg[]
    bot.sendMessage(msg['chat']['id'], msg['chat']['first_name']+" "+msg['chat']['last_name']+" say: "+msg['text'])

# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
