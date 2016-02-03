import sys
import time
import pprint
import telepot

def handle(msg):
    print(msg)
    # Do your stuff here ...
    #postmsg=msg[]
    if 'forward_from' in msg.keys():
        bot.sendMessage(msg['from']['id'], "\""+msg['from']['first_name']+" "+msg['from']['last_name']+"\" foward the msg of \""+msg['forward_from']['first_name']+" "+msg['forward_from']['last_name']+"\" that said: \n"+msg['text'])
    else:
        bot.sendMessage(msg['from']['id'], msg['from']['first_name']+" "+msg['from']['last_name']+" say: "+msg['text'])

# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
