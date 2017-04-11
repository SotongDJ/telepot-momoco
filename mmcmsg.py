import tool, json

def chstr(a,b,c,d): # if a == b, return c; else return d
    if a == b :
        return c
    else:
        return d

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.start())
"""
def start():
    final="""  Welcome
----------------------------
This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Pls setup before using:
  Account setup = /set_Account
  Currency setup = /set_Currency
----------------------------
    /help    /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.help())
"""
def help():
    final="""  Help
----------------------------
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
----------------------------

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.setting())
"""
def setting(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Setting Card
----------------------------
Account Setting:
    /set_Account
Currency Setting:
    /set_Currency
----------------------------
P.S. You still can use the last card

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.newStart(self._mem,keywo))
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            keywo = ""
"""
def newStart(dicto,keywo):
    final="""New Record
----------------------------
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

----------------------------
Keyword: """+keywo+"""
/set_as_Date (format: yyyy-mm-dd) /set_as_Product /set_as_Class /set_as_Seller /set_as_Price
----------------------------
/Discard /Save /List /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.newConti(self._mem,keywo))
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            keywo = ""
"""
def newConti(dicto,keywo):
    final="""Filling the blank (Creating Card)
----------------------------
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

----------------------------
Keyword: """+keywo+"""
/set_as_Date (format: yyyy-mm-dd) /set_as_Product /set_as_Class /set_as_Seller /set_as_Price
----------------------------
/Discard /Save /List /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.newConti(self._mem))
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
"""
def newFinis(dicto):
    final="""New Record Saved (Creating Card)
----------------------------
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

----------------------------
/Edit  /List  /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.newDiscard())
"""
def newDiscard():
    final="""¡ Discard !
----------------------------

    Closed Creating Card

----------------------------
  /Whats_Now  /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.lisFilte(self._mem))


"""
def lisFilte(dicto):
    final="""Filtering Card (Listing Card)
----------------------------
Date range:"""+dicto["datte"]+"""
/Today /This_Week
/This_Month /This_Year

----------------------------
/Discard  /Sumit  /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.lisDiscard())
"""
def lisDiscard():
    final="""¡ Discard !
----------------------------

    Closed Listing Card

----------------------------
  /Whats_Now  /Setting

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.home(keywo))
            keywo = ""
"""
def home(keywo): # will replace by Start Card after finished Account Card and Currency Card
    final="""Home Card (Temporary)
----------------------------
Welcome Home !
Keyword : """+keywo+"""
    /New    /List
----------------------------
    /Setting    /help

This chatbot is under constructing...
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.timesout())
"""
def timesout(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Time's Out
----------------------------
Previous unsave work was clean out.

This chatbot is under constructing...
"""
    return final
