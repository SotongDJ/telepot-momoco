import tool, json, mmctool

def short(tasta):
    dicta={
        'presys':'This chatbot is UNDER CONSTRUCTING\n——————————\n',
        'con':'Create New Conversation',
        'cof':'～～～～～～～～～～\nConversation Closed\n(Key word to start a new conv.)',
        'refeson':'This chatbot is UNDER CONSTRUCTING\n——————————\nRefreshing database...',
        'refesfin':'Refreshing Finished !\n～～～～～～～～～～\n',
        'rekeswd':'～～～～～～～～～～\nGive me a word or a number',
        'bye':'See you next time! Bye!\n(Conversation Closed !)',
        'rgsWarn':"The keyword that you selected doesn't Exist or Expired\n～～～～～～～～～～\n",
        'whatsnow':"Try /whats_now ",
        'analitempo':'abratio => dtempo,utempo,conda,conde,targe\natren => dtempo,utempo,leve,conda,conde',
        'analiWarn':"Fill in all the spaces",
        'band':'～～～～～～～～～～\n',
    }
    return dicta.get(tasta,'')
""" self.sender.sendMessage(mmcmsg.start()) """
def start():
    final="""　Welcome
——————————
This is Money Money Come Chatbot.
It can help you to trace your money flow moreeasily (Sure? )

Notes:
　/setting
　　Please Setup before using
——————————
　/help
"""
    return final

""" self.sender.sendMessage(mmcmsg.help())"""
def help():
    final="""　Help card (Command List)
——————————
　/help
　　Show command list
　/whats_now
　　Show current unsaved work
　/new
　　Create new record
　/list
　　Show prevous record
　/statics
　　View statistics card
　/start
　　Welcome and Introduction
　/setting
　　View setting card
　/exit
　　Close conversation
"""
    return final

""" self.sender.sendMessage(mmcmsg.bored())"""
def bored():
    final="""My "Job"　[ I am free ~ ]
——————————
　/start
　　Welcome Card
　/new
　　Creating New Record
　/list
　　Review Card
　/statics
　　Analystic Card
　/setting
　　Setting Card
"""
    return final

""" self.sender.sendMessage(mmcmsg.selection(self._defSett,'Account'))"""
def selection(txt,titil):
    final="Select "+titil+"""
——————————
"""+titil+""" List:
"""+txt+"""
——————————
　/Discard /Save　/Back
Remind:
　Select above or type another selection
"""
    return final


""" self.sender.sendMessage(mmcmsg.home(self._keywo)) """
def home(keywo): # will replace by Start Card after finished Account Card and Currency Card
    final="""Keyword Card
——————————
I received your keyword:
　"""+keywo+"""

What do you want to do?
　/new　/list

　/statics
——————————
　/setting　/help
"""
    return final

""" self.sender.sendMessage(mmcmsg.timesout()) """
def timesout(): # will replace by Start Card after finished Account Card and Currency Card
    final="""Time's Out
——————————
Previous unsave work was CLEAN OUT.
"""
    return final

def error():
    final=""""Status
——————————
Received wrong message
Input:
　Undetactable content type
"""
    return final
