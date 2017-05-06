import tool, json
import mmctool
# incoMsg : main(), keyword(), finis()
# outoMsg : recom(), discard()

def main(dicto):
    final="""New Transfer Card
——————————
Date: """+dicto["datte"]+"""
Remind: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Place: """+dicto["shoop"]+"""
　　——————　　
Transfer from which Account:
"""+mmctool.chstr(dicto["fromm"],"","    ( /change_Acc_From )",'    '+dicto["fromm"]+"  ( /change_Acc_From )")+"""
Amount(From) : """+dicto["karen"]+" "+dicto["price"]+"""
    ( /change_Currency )
　　——————　　
Transfer to which Account:
"""+mmctool.chstr(dicto["toooo"],"","    ( /change_Acc_To )",'    '+dicto["toooo"]+"  ( /change_Acc_To )")+"""
Amount(To) : """+dicto["tkare"]+" "+dicto["tpric"]+"""
( /change_Currency_To )
　　——————　　
Notes:
"""+dicto["desci"]+"""
——————————
  /change_to_Expense
    Change to Expense Card
  /change_to_Income
    Change to Income Card
——————————
  /Discard  /Save  /setting
——————————
P.S. Give me a word or a number
"""
    return final

def keyword(keywo):
    final="""Filling the blank
——————————
Keyword:
  """+keywo+"""

  /set_as_Date  /set_as_Place
    (Format of Date: yyyy-mm-dd)
  /set_as_Remind  /set_as_Notes
——————————
  /set_as_Account_From

  /set_as_Amount_From

  /set_as_Currency_Source
——————————
  /set_as_Account_To

  /set_as_Amount_To

  /set_as_Currency_Target
——————————
  /Discard  /Save  /setting

"""
    return final

def finis(dicto):
    final="""New #Transfer Record #Saved
——————————
Date: """+dicto["datte"]+"""
Remind: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Place: """+dicto["shoop"]+"""
Amount(From) : """+dicto["karen"]+" "+dicto["price"]+"""
Amount(To) : """+dicto["tkare"]+" "+dicto["tpric"]+"""
Transfer from which Account:
"""+dicto["fromm"]+"""
Transfer to which Account:
"""+dicto["toooo"]+"""
Notes:
"""+dicto["desci"]+"""
——————————
  /Edit  /list  /setting

"""
    return final
