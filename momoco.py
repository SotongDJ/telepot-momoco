import tool, json

def check(file_name):
    a=open(file_name,"r")
    b=json.load(a)
    for n in b.keys():
        print(n)
        for m in b[n].keys():
            print("    "+m+" : "+b[n][m])

def ask(self,text):
    if "/start" in text:
        self.sender.sendMessage("""Welcome!
This is Money Money Come Chatbot.
It can help you to trace your money flow more easily (Sure?)
Reply /help to learn more~""")
    elif "/help" in text:
        self.sender.sendMessage("""This chatbot is under constructing...
Reply:
/setting to change the setting
""")
    elif "/List" in text:
        self.sender.sendMessage("""List :
Filter by Time:
/All /Day /Week /Year
Filter by Class:
/All /"""+" /".join(self._lem["klass"])+"""
Filter by Seller:
/All /"""+" /".join(self._lem["shoop"])+"""
Filter by Account:
/All /"""+" /".join(self._lem["accnt"])+"""
Filter by Currency:
/All /"""+" /".join(self._lem["karen"])+"""
----------------------------------------------
/Discard to discard changes or cancel
""")
