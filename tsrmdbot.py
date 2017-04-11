import sys, os, time, telepot, json, tool, auth, log

#def respon(msg):

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    datetime = str(msg['date'])
    datetimeInt=msg['date']
    logmsg="Receive Msg: "+msg['text']+"\n        content_type="+content_type+", chat_type="+chat_type+", chat_id="+str(chat_id)+", date="+datetime
    log.logging(auth.id(),logmsg,"tsrmdbot")

    if content_type == 'text':
        if msg['text']=="/start":
            startmsg=tool.msg("tsrmd-start")
            bot.sendMessage(chat_id,startmsg)
        elif msg['text']=="/admin":
            warnMsg="User "+str(chat_id)+"  is mentioning you, pls /reply_"+str(chat_id)
            bot.sendMessage(auth.id(),warnMsg)

        elif chat_id == auth.id():
            if msg['text']=="/help":
                helpmsg=tool.msg("tsrmd-help")
                bot.sendMessage(chat_id, helpmsg)

            elif msg['text']=="/temp":
                os.system("/opt/vc/bin/vcgencmd measure_temp>./database/temp")
                bot.sendMessage(chat_id,open("./database/temp").read())
            else:
                bot.sendMessage(chat_id, "unrecgonizable command, Original message:\n\""+msg['text']+"\"")

        else:
            bot.sendMessage(chat_id, "Required permission, Original message:\n\""+msg['text']+"\"")

    elif content_type == 'document':
            if msg["document"]["file_name"] == "bin.tar.gz":
                os.system("rm bin.tar.gz")
                bot.download_file(msg["document"]["file_id"],"./bin.tar.gz")
                bot.sendMessage(auth.id(), "Server updating ... ")
                os.system("setsid ./upgrade.sh")
    else:
        bot.sendMessage(chat_id, "No action, No response")
key=json.load(open("database/key","r"))
TOKEN = key["tsrmdbot"]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
#
bootmsg="Server Starting,\nListening ..."
bot.sendMessage(auth.id(), bootmsg)
log.logging(auth.id(),bootmsg,"tsrmdbot")

# Keep the program running.
while 1:
    time.sleep(10)
