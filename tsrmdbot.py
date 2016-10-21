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

    if auth.admin(chat_id):
        if content_type == 'text':
            if msg['text']=="/help":
                helpmsg=externa.msg("tsrmd-help")
                bot.sendMessage(chat_id, helpmsg)

            elif msg['text']=="/start":
                startmsg=externa.msg("tsrmd-start")
                bot.sendMessage(chat_id,startmsg)

            elif msg['text']=="/mode":
                bot.sendMessage(chat_id,"Current mode is \""+moda+"\"")

            elif msg['text']=="/quit":
                externa.change("mode","none",chat_id)
                bot.sendMessage(chat_id,"Successfully quit mode from \""+moda+"\"")

            elif msg['text']=="/temp":
                os.system("/opt/vc/bin/vcgencmd measure_temp>./database/temp")
                bot.sendMessage(chat_id,open("./database/temp").read())

            elif msg['text']=="/admin":
                bot.sendMessage(chat_id,auth.check().read())

            elif msg['text']=="/restart":
                #remsg=externa.msg("tsrmd-restart")
                #bot.sendMessage(chat_id, remsg)
                os.system("setsid ./restart.sh "+target)
            #elif msg['text']=="/re-":
            #    target=msg['text'].split("-")[1]
            #    os.system("setsid ./restart.sh "+target)

            else:
                bot.sendMessage(chat_id, "No action, Original message:\n\""+msg['text']+"\"")
        elif content_type == 'document':
            if msg["document"]["file_name"] == "bin.tar.gz":
                os.system("rm bin.tar.gz")
                bot.download_file(msg["document"]["file_id"],"./bin.tar.gz")
                bot.sendMessage(auth.id(), "Admin is updating Server ")
                os.system("setsid ./upgrade.sh")
    else:
        bot.sendMessage(chat_id, "No action, No response")
TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
#
bot.sendMessage(auth.id(), "Server Starting")
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
