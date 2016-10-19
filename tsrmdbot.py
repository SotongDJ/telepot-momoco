import sys
import os
import time
import telepot
import externa
import id4feel
import auth
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    datetime = str(msg['date'])
    datetimeInt=msg['date']
    print(content_type, chat_type, chat_id, datetime)
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

        elif msg['text']=="/pull":
            bot.sendMessage(chat_id,open(externa.path("analisi/feel",str(chat_id))+"record.csv").read())

        elif msg['text']=="/keywo":
            if moda == "analisi/feel":
                bot.sendMessage(chat_id,open("./database/keywo/"+moda+"/dicto").read())
                bot.sendMessage(chat_id,open("./database/keywo/"+moda+"/dikta").read())

        elif msg['text']=="/temp":
            if auth.admin(chat_id):
                os.system("/opt/vc/bin/vcgencmd measure_temp>./database/temp")
                bot.sendMessage(chat_id,open("./database/temp").read())

        elif moda == "analisi/feel":
            mark=id4feel.idenFeel(msg['text'])
            level=mark['level']
            limit=mark['limit']
            keywos=mark['keyword']
            print("level="+str(level)+", limit="+str(limit))
            if abs(level) > limit:
                fif=open(externa.path("analisi/feel",str(chat_id))+"record.csv","a")
                fif.write(str(chat_id)+","+datetime+","+"-".join(keywos)+","+str(level)+",\""+msg['text']+"\",\""+time.asctime(time.localtime(datetimeInt))+"\"\n")
                fif.close()
                bot.sendMessage(chat_id, "Recorded, Original message:\n\""+msg['text']+"\"")
            elif level != 0:
                bot.sendMessage(chat_id, "Recognized but lower the threshold, Original message:\n\""+msg['text']+"\"")
            elif level == 0:
                bot.sendMessage(chat_id, "Can't recognize, Original message:\n\""+msg['text']+"\"")

        else:
            bot.sendMessage(chat_id, "No action, Original message:\n\""+msg['text']+"\"")
    elif content_type == 'document':
        if auth.admin(chat_id):
            if msg["document"]["file_name"] == "bin.tar.gz":
                os.system("rm bin.tar.gz")
                bot.download_file(msg["document"]["file_id"],"./bin.tar.gz")
    else:
        bot.sendMessage(chat_id, "No action, No response")
TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
#
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
