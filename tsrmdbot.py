import sys
import os
import time
import telepot
import externa
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    datetime = str(msg['date'])
    print(content_type, chat_type, chat_id)
    os.system("mkdir -p ./database/"+str(chat_id)+"/")
    moda=externa.check("mode",chat_id)

    if moda == "":
        externa.change("mode","none",chat_id)

    if content_type == 'text':
        if msg['text']=="/help":
            helpmsg=externa.msg("help")
            bot.sendMessage(chat_id, helpmsg)

        elif msg['text']=="/start":
            startmsg=externa.msg("start")
            bot.sendMessage(chat_id,startmsg)

        elif msg['text']=="/mode":
            bot.sendMessage(chat_id,"Current mode is \""+moda+"\"")

        elif msg['text']=="/feel":
            externa.change("mode","analisi/feel",chat_id)
            bot.sendMessage(chat_id,"Mode change from \""+moda+"\" to \"Analisi/Feel\"")

        elif msg['text']=="/quit":
            externa.change("mode","none",chat_id)
            bot.sendMessage(chat_id,"Successfully quit mode from \""+moda+"\"")

        elif moda == "analisi/feel":
            level=0
            limit=1
            plus=2
            for keyword in ["Feel","feel"]:
                if keyword in msg['text']:
                    level=level+plus
            print("level="+str(level)+", limit="+str(limit))
            if level > limit:
                fif=open(externa.path("analisi/feel",str(chat_id))+"feeling.csv","a")
                fif.write(str(chat_id)+","+datetime+",\""+msg['text']+"\"\n")
                fif.close()
                bot.sendMessage(chat_id, "Recorded, Original message:\n\""+msg['text']+"\"")
            elif level > 0:
                bot.sendMessage(chat_id, "Recognized but lower the threshold, Original message:\n\""+msg['text']+"\"")
            elif level == 0:
                bot.sendMessage(chat_id, "Can't recognize, Original message:\n\""+msg['text']+"\"")

        else:
            bot.sendMessage(chat_id, "No action, Original message:\n\""+msg['text']+"\"")

    else:
        bot.sendMessage(chat_id, "No action, Original message:\n\""+msg['text']+"\"")
TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
#
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
