import tool, json
import mmctool
# outoMsg : main(), keyword(), recom(), finis(), discard()

""" self.sender.sendMessage(mmcmsg.outo(self._temra)) """
def main(dicto):
    final="""New Expense Card
——————————
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
　　——————　　
Spent:
　"""+dicto["karen"]+" "+dicto["price"]+' ('+dicto["fromm"]+""")
　［Price (Account)］
　/change_Currency

　/change_Acc_From
　　——————　　
Notes:
"""+dicto["desci"]+"""
——————————
　/change_to_Income
　　Change to Income Card
　/change_to_Transfer
　　Change to Transfer Card
——————————
　/Discard　/Save　/setting
"""
    return final

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
　/Discard　/Save　/setting
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

""" self.sender.sendMessage(mmcmsg.outoConti(self._temra)) """
def finis(dicto):
    final="""New #Expense Record #Saved
——————————
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
　　——————　　
Spent: """+dicto["karen"]+" "+dicto["price"]+' ('+dicto["fromm"]+""")
　　——————　　
Notes:
"""+dicto["desci"]+"""
——————————
　/Edit　/list　/setting
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
