import tool, json

def chstr(a,b,c): # if a == "", return b; else return c
    if a == "" :
        return b
    else:
        return c

def start(self):
    final="""  Welcome
----------------------------------------------
This is Money Money Come Chatbot.
It can help you to trace your money flow more
easily (Sure? )

Pls setup before using:
    Account setup = /set_Account
    Currency setup = /set_Currency
----------------------------------------------
    /help    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)

def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "

    elif comme == "help":
        final="""  Help
----------------------------------------------
/start
    Welcome Card
/help
    Command List Card
/New
    Creating  Card
/List
    Record Showing Card
/Setting
    Setting Card
----------------------------------------------

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)
def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "

    elif comme == "newStart":
        final="""New Record
----------------------------------------------
Date: """+dicto["datte"]+"""
Product: """+dicto["namma"]+"""
Class: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["price"]+"""

Currency: """+dicto["karen"]+"""
    ( /change_Currency )

Spent from which Account:
"""+chstr(dicto["fromm"],"    ( /choose_Acc_From )",dicto["fromm"]+"\n    ( /choose_Acc_From )")+"""

Transfer to which Account: (if have)
"""+chstr(dicto["toooo"],"    ( /choose_Acc_To )",dicto["toooo"]+"\n    ( /choose_Acc_To )")+"""

----------------------------------------------
Keyword: """+dicto["text"]+"""
    /set_as_Date (format: yyyy-mm-dd)
    /set_as_Product /set_as_Class
    /set_as_Seller /set_as_Price
----------------------------------------------
    /Discard    /Save    /List    /Setting

This chatbot is under constructing...
"""

    self.sender.sendMessage(final)
def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "

    elif comme == "newConti":
        final="""Filling the blank
----------------------------------------------
Date: """+dicto["datte"]+"""
Product: """+dicto["namma"]+"""
Class: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["price"]+"""

Currency: """+dicto["karen"]+"""
    ( /change_Currency )

Spent from which Account:
"""+chstr(dicto["fromm"],"    ( /choose_Acc_From )",dicto["fromm"]+"\n    ( /choose_Acc_From )")+"""

Transfer to which Account: (if have)
"""+chstr(dicto["toooo"],"    ( /choose_Acc_To )",dicto["toooo"]+"\n    ( /choose_Acc_To )")+"""

----------------------------------------------
Keyword: """+dicto["text"]+"""
    /set_as_Date (format: yyyy-mm-dd)
    /set_as_Product /set_as_Class
    /set_as_Seller /set_as_Price
----------------------------------------------
    /Discard    /Save    /List    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)
def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "


    elif comme == "newFinish":
        final="""New Record Saved
----------------------------------------------
Date: """+dicto["datte"]+"""
Product: """+dicto["namma"]+"""
Class: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["price"]+"""

Currency: """+dicto["karen"]+"""

Spent from which Account:
"""+dicto["fromm"]+"""

Transfer to which Account: (if have)
"""+dicto["toooo"]+"""

----------------------------------------------
    /Edit    /List    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)
def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "

    elif comme == "listFilter":
        final="""Filtering Card
----------------------------------------------
Date range:"""+dicto["datte"]+"""
/Today /This_Week /This_Month /This_Year

----------------------------------------------
    /Discard    /Summit    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)
def msg(self,comme,msg,dicto):
    final="Error: missing 'comme' "

    elif comme == "home": # will replace by Start Card after finished Account Card and Currency Card
        final="""Home Card (Temporary)
----------------------------------------------
Welcome Home !
Keyword : """+"""
----------------------------------------------
    /Discard    /Summit    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)

# Above : Recvontruction
# Below : Old

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
