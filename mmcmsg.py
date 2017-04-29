import tool, json, mmcdb, mmctool

def warn():
    final = "This chatbot is under constructing..."
    return final

""" self.sender.sendMessage(mmcmsg.start()) """
def start():
    final="""  Welcome
----------------------------

This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Pls setup before using:
  /modify_Setting
    Account setup
  /set_Currency
    Currency setup
----------------------------
  /help  /Setting
"""
    return final

""" self.sender.sendMessage(mmcmsg.help())"""
def help():
    final="""  Help
----------------------------
  /start
    Welcome Card
  /help
    Command List Card
  /New
    Creating New Card
  /List
    Review Card
  /Statics
    Analytic Card
  /Setting
    Setting Card
  /Whats_Now
    Check current work status
"""
    return final

""" self.sender.sendMessage(mmcmsg.setting()) """
def setting(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Setting Card
----------------------------
Account Setting:
  /modify_Setting
Currency Setting:
  /set_Currency
----------------------------
P.S. You still can use the last card
  /Whats_Now
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.defSettList(self._setting))
"""
def defSettList(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting Card
----------------------------
Default Income: (E.g. Bank Account)
  """+setting['dinco']+""" /change_i

Default Expense: (E.g. Cash)
  """+setting['dexpe']+""" /change_e
----------------------------
General Income Source:(E.g. Income)
  """+setting['genis']+""" /change_g

Overall Expense Destination: (E.g. Expense)
  """+setting['ovede']+""" /change_o
----------------------------
Normal Income:
    G.I.S. ---> Bank A Account
Normal Expense:
    Cash ---> O.E.D.
Withdrawal:
    Bank A ---> Cash
Deposit:
    Cash ---> Bank A
Tranfer:
    Bank A ---> Bank B
----------------------------
    /Discard /Save
Note: Changing setting now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettSel(self._defSett,'Account Setting Card'))"""
def defSettSel(txt,titil):
    final=titil+"""
----------------------------
Account List:
"""+txt+"""
----------------------------
    /Discard /Save  /modify_Setting
P.S. Select above or type another selection
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.defSettSet())

"""
def defSettSet(keywo,teksi):
    final="""Select Position
----------------------------
Keyword: """+keywo+"""

Position:
    Default Income
        ( """+teksi[1][0]+"i"+teksi[1][1]+""" )
    Default Expense
        ( """+teksi[1][0]+"e"+teksi[1][1]+""" )
    General Income Source
        ( """+teksi[1][0]+"g"+teksi[1][1]+""" )
    Overall Expense Destination
        ( """+teksi[1][0]+"o"+teksi[1][1]+""" )
----------------------------
  /Discard  /Save /modify_Setting

"""
    return final

""" self.sender.sendMessage(mmcmsg.defAccFins(self._setting))"""
def defAccFins(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting #Saved
----------------------------
Default Income: """+setting['dinco']+"""
Default Expense: """+setting['dexpe']+"""
General Income Source: """+setting['genis']+"""
Overall Expense Destination: """+setting['ovede']+"""
----------------------------
    /Setting /Help /Whats_Now
Note: Changing setting now
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.defAccDis())
"""
def defAccDis():
    final="""¡ Discard !
----------------------------

  Closed Account Setting Card

----------------------------
  /Setting  /help
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outo(self._temra))
            self._temra = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            keywo = ""
"""
def outo(dicto):
    final="""New Expense Card
----------------------------
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["karen"]+" "+dicto["price"]+"""
    ( /change_Currency )
Spent from which Account:
"""+mmctool.chstr(dicto["fromm"],"","    ( /choose_Acc_From )",dicto["fromm"]+"\n    ( /choose_Acc_From )")+"""
Notes:
"""+dicto["desci"]+"""
----------------------------
  /change_to_Income
    Change to Income Card
  /change_to_Transfer
    Change to Transfer Card
----------------------------
  /Discard  /Save  /List  /Setting
----------------------------
P.S. Give me a word or a number
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoKeywo(keywo))
            keywo = ""
"""
def outoKeywo(keywo):
    final="""Filling the blank
----------------------------
Keyword:
  """+keywo+"""

  /set_as_Date
    (format: yyyy-mm-dd)
  /set_as_Item

  /set_as_Category

  /set_as_Seller

  /set_as_Price

  /set_as_Notes
----------------------------
  /Discard  /Save  /List  /Setting

"""
    return final

""" self.sender.sendMessage(mmcmsg.outoRecom(self._temra,self._keys,self._keywo,self._fs,chat_id))
            namma, klass, shoop, price"""
def outoRecom(txt,keywo):
    final="""Recommend Card
----------------------------

Last Keyword: (Typing)
    """+keywo+"""
Recommend List:
"""+txt+"""

----------------------------
  /Discard  /Save  /List  /Setting
P.S. Choose above or type another keyword
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoConti(self._temra))
            self._temra = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
"""
def outoFinis(dicto):
    final="""New #Expense Record #Saved
----------------------------
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["karen"]+" "+dicto["price"]+"""
Spent from which Account:
"""+dicto["fromm"]+"""
Notes:
"""+dicto["desci"]+"""
----------------------------
  /Edit  /List  /Setting

"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.outoDiscard())
"""
def outoDiscard():
    final="""¡ Discard !
----------------------------

  Closed Creating Card

----------------------------
  /Setting  /help
"""
    return final

""" self.sender.sendMessage(mmcmsg.listMain(self._temra)) """
def listMain(dicto):
    final="""Listing Card
----------------------------
Date:"""+dicto["datte"]+"""
List:
"""+"""
----------------------------
Current Mode:
    """+"""
  /change_Range
----------------------------
  /Discard
"""
    return final

""" self.sender.sendMessage(mmcmsg.listSect(uuid,usrid,libra)) """
def listSect(uuid,usrid,libra):
    final="""Single record Card
----------------------------
ID: """+"""
Date: """+libra['raw'][uuid]["datte"]+"""
Item: """+libra['raw'][uuid]["namma"]+"""
Category: """+libra['raw'][uuid]["klass"]+"""
Seller: """+libra['raw'][uuid]["shoop"]+"""
"""+"""
Price: """+libra['raw'][uuid]["karen"]+" "+libra['raw'][uuid]["price"]+"""
Spent from which Account:
"""+libra['raw'][uuid]["fromm"]+"""
Transfer to which Account:
"""+libra['raw'][uuid]["toooo"]+"""
"""+libra['raw'][uuid]["tkare"]+" "+libra['raw'][uuid]["tpric"]+"""

"""+"""Notes:
"""+dicto["desci"]+"""
----------------------------
   /List  /Edit  /Delete  /Setting

"""
    return final

""" self.sender.sendMessage(mmcmsg.listDisca()) """
def listDisca():
    final="""¡ Discard !
----------------------------

  Closed Listing Card

----------------------------
  /Whats_Now  /Setting
"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.home(self._keywo))
            self._keywo=""
"""
def home(keywo): # will replace by Start Card after finished Account Card and Currency Card
    final="""Home Card (Temporary)
----------------------------

    Welcome Home !

Keyword: """+keywo+"""
  /New  /List
----------------------------
  /Setting  /help

"""
    return final

"""--------------------------------------------------------
        self.sender.sendMessage(mmcmsg.timesout())
"""
def timesout(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Time's Out
----------------------------

Previous unsave work was clean out.

"""
    return final

def error():
    final=""""Status:
Received wrong message
Input:
    Undetactable content type
"""
    return final
