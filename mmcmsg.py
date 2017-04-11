import tool, json

def chstr(a,b,c,d): # if a == b, return c; else return d
    if a == b :
        return c
    else:
        return d

"""--------------------------------------------------------
        mmcmsg.start()
"""
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

"""--------------------------------------------------------
        mmcmsg.help()
"""
def help(self):
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

"""--------------------------------------------------------
        mmcmsg.newStart(self._mem,self._tem)
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            self._tem = ""
"""
def newStart(self,dicto,keywo):
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
Keyword: """+keywo+"""
    /set_as_Date (format: yyyy-mm-dd)
    /set_as_Product /set_as_Class
    /set_as_Seller /set_as_Price
----------------------------------------------
    /Discard    /Save    /List    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)

"""--------------------------------------------------------
        mmcmsg.newConti(self._mem,self._tem)
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
            self._tem = ""
"""
def newConti(self,dicto,keywo):
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
Keyword: """+keywo+"""
    /set_as_Date (format: yyyy-mm-dd)
    /set_as_Product /set_as_Class
    /set_as_Seller /set_as_Price
----------------------------------------------
    /Discard    /Save    /List    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)

"""--------------------------------------------------------
        mmcmsg.newConti(self._mem)
            self._mem = {
                "namma":"", "klass":"", "shoop":"",
                "datte":"", "price":"",
                "karen":"",
                "fromm":"", "toooo":"",
            }
"""
def newFinis(self,dicto):
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

"""--------------------------------------------------------
        mmcmsg.lisFilte(self._mem,self._tem)


"""
def lisFilte(self,dicto):
    final="""Filtering Card
----------------------------------------------
Date range:"""+dicto["datte"]+"""
/Today /This_Week /This_Month /This_Year

----------------------------------------------
    /Discard    /Summit    /Setting

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)

"""--------------------------------------------------------
        mmcmsg.home(self._tem)
            self._tem = ""
"""
def home(self,keywo): # will replace by Start Card after finished Account Card and Currency Card
    final="""Home Card (Temporary)
----------------------------------------------
Welcome Home !
Keyword : """+keywo+"""
    /New    /List
----------------------------------------------
    /Setting    /help

This chatbot is under constructing...
"""
    self.sender.sendMessage(final)
