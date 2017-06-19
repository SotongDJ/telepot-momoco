import tool, json
import mmctool
# msgOuto : main(), keyword(), recom(), finis(), discard()

""" self.sender.sendMessage(mmcmsg.outoKeywo(keywo)) """
def keyword(keywo):
    final="""Filling the blank
——————————
Keyword:
　"""+keywo+"""

　/set_as_Date
(Format of Date: yyyy-mm-dd)
　/set_as_Item　/set_as_Category

　/set_as_Seller　/set_as_Notes
——————————
　/set_as_Price　/set_as_Account

　/set_as_Currency_Source
——————————
　/Discard　/whats_now
"""
    return final

""" self.sender.sendMessage(self._recom[1],self._keywo) """
def recom(txt,keywo):
    final="""Recommend Card
——————————
Last Keyword: (Typing)
　　"""+keywo+"""
Recommend List:
"""+txt+"""
——————————
　/Discard　/Save　/setting
Remind:
　Choose above or type another keyword
"""
    return final

""" self.sender.sendMessage(mmcmsg.outoDiscard()) """
def discard():
    final="""¡ Discard !
——————————

　Closed Creating Card

——————————
　/setting　/help
"""
    return final
