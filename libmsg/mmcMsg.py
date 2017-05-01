import tool, json, mmctool

def warn():
    final = "This chatbot is under constructing..."
    return final

""" self.sender.sendMessage(mmcmsg.start()) """
def start():
    final="""  Welcome
----------------------------

This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Notes:
  /Setting
    Please Setup before using
----------------------------
  /help
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
    Creating New Record
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

""" self.sender.sendMessage(mmcmsg.bored())"""
def bored():
    final="""  I am free ~
------------------
My "Job"
------------------
  /start
    Welcome Card
  /New
    Creating New Record
  /List
    Review Card
  /Statics
    Analystic Card
  /Setting
    Setting Card
"""
    return final

""" self.sender.sendMessage(mmcmsg.selection(self._defSett,'Account'))"""
def selection(txt,titil):
    final="Select "+titil+"""
----------------------------
"""+titil+""" List:
"""+txt+"""
----------------------------
    /Discard /Save  /Back
P.S. Select above or type another selection
"""
    return final


""" self.sender.sendMessage(mmcmsg.home(self._keywo)) """
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

""" self.sender.sendMessage(mmcmsg.timesout()) """
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
