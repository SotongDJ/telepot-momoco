import sys
import os
import time
import telepot
import externa
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    moda=externa.check("mode",chat_id)
    if moda == "":
        externa.change("mode","none",chat_id)
    if moda == "feel-analisi":
        os.system("mkdir "+externa.path("analisi",str(chat_id)))
        if content_type == 'text':
            if "feel" in msg['text']:
                fif=open(externa.path("analisi",str(chat_id))+"feeling.csv","a")
                fif.write(str(chat_id)+",\""+msg['text']+"\"\n")
                fif.close()
                bot.sendMessage(chat_id, msg['text'])
    elif moda == "none":
        if content_type == 'text':
            if msg['text']=="/help":
                bot.sendMessage(chat_id, "Commands:\n/help\n    Show this document\n/start\n    Choose moda\n")
            elif msg['text']=="/feel":
                bot.sendMessage(chat_id,"Mode change from \""+moda+"\" to \"feel-analisi\"")
            elif msg['text']=="/mode":
                bot.sendMessage(chat_id,"Current mode is \""+moda+"\"")
            else:
                bot.sendMessage(chat_id, msg['text'])

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
#
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
