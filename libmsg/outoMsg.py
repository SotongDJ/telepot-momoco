import tool, json
import mmctool
# outoMsg : main(), keyword(), recom(), finis(), discard()

""" self.sender.sendMessage(mmcmsg.outo(self._temra)) """
def main(dicto):
    final="""New Expense Card
----------------------------
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
Price: """+dicto["karen"]+" "+dicto["price"]+"""
    ( /change_Currency )
Spent from which Account:
"""+mmctool.chstr(dicto["fromm"],"","    ( /change_Acc_From )",'    '+dicto["fromm"]+"  ( /change_Acc_From )")+"""
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

""" self.sender.sendMessage(mmcmsg.outoKeywo(keywo)) """
def keyword(keywo):
    final="""Filling the blank
----------------------------
Keyword:
  """+keywo+"""

  /set_as_Date
    (Format of Date: yyyy-mm-dd)
  /set_as_Item  /set_as_Category

  /set_as_Seller  /set_as_Price

  /set_as_Notes
----------------------------
  /Discard  /Save  /List  /Setting

"""
    return final

""" self.sender.sendMessage(self._recom[1],self._keywo) """
def recom(txt,keywo):
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

""" self.sender.sendMessage(mmcmsg.outoConti(self._temra)) """
def finis(dicto):
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

""" self.sender.sendMessage(mmcmsg.outoDiscard()) """
def discard():
    final="""¡ Discard !
----------------------------

  Closed Creating Card

----------------------------
  /Setting  /help
"""
    return final
