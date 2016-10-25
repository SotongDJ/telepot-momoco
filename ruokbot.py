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
    moda=externa.check("mode",chat_id)

    if moda == "":
        externa.change("mode","analisi/feel",chat_id)
    elif moda == "none":
        externa.change("mode","analisi/feel",chat_id)

    if content_type == 'text':
        if msg['text']=="/help":
            helpmsg=externa.msg("ruok-help")
            bot.sendMessage(chat_id, helpmsg)

        elif msg['text']=="/start":
            startmsg=externa.msg("ruok-start")
            bot.sendMessage(chat_id,startmsg)

        elif msg['text']=="/mode":
            bot.sendMessage(chat_id,"Current mode is \""+moda+"\"")

        elif msg['text']=="/feel":
            externa.change("mode","analisi/feel",chat_id)
            bot.sendMessage(chat_id,"Mode change from \""+moda+"\" to \"Analisi/Feel\"")

        elif msg['text']=="/quit":
            externa.change("mode","none",chat_id)
            bot.sendMessage(chat_id,"Successfully quit mode from \""+moda+"\"")

        elif msg['text']=="/result":
            if moda == 'none':
                bot.sendMessage(chat_id,"No result")
            else:
                bot.sendMessage(chat_id,open(externa.path(moda,str(chat_id))+"record.csv").read())

        elif msg['text']=="/keywo":
            if moda == "analisi/feel":
                bot.sendMessage(chat_id,open("./database/keywo/"+moda+"/dicto").read())
                bot.sendMessage(chat_id,open("./database/keywo/"+moda+"/dikta").read())
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
    toyear,tomonth,today,tohour,tomin,tosec,widay,yeday,isds=time.localtime()
    if tomin == 0:
        if tohour in [8,12,18,20]:
            for userid in auth.user():
                bot.sendMessage(userid, "What is your feeling now?")
    time.sleep(60)
