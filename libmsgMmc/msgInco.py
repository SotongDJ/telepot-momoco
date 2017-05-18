import tool, json
import mmctool
# msgInco : main(), keyword(), finis()
# msgOuto : recom(), discard()

def main(dicto):
    final="""New Income Card
——————————
Date: """+dicto["datte"]+"""
Remind: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Agent: """+dicto["shoop"]+"""
　/change_Agent
　　——————　　
Income:
　"""+dicto["tkare"]+" "+dicto["tpric"]+' ('+dicto["toooo"]+""")
　［Price (Account)］
　/change_Currency_To

　/change_Acc_To
　　——————　　
Notes:
"""+dicto["desci"]+"""
——————————
　/change_to_Expense
　　Change to Expense Card
　/change_to_Transfer
　　Change to Transfer Card
——————————
　/Discard　/Save　/setting
"""
    return final

def keyword(keywo):
    final="""Filling the blank
——————————
Keyword:
　"""+keywo+"""

　/set_as_Date　/set_as_Agent　
(Format of Date: yyyy-mm-dd)
　/set_as_Remind　/set_as_Notes
　　——————　　
　/set_as_Account_To　/set_as_Income

　/set_as_Currency_Target
——————————
　/Discard　/whats_now
"""
    return final

def finis(dicto):
    final="""New #Income Record #Saved
——————————
Date: """+dicto["datte"]+"""
Remind: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Agent: """+dicto["shoop"]+"""
　　——————　　
Income: """+dicto["tkare"]+" "+dicto["tpric"]+' ('+dicto["toooo"]+""")
　　——————　　
Notes:
"""+dicto["desci"]+"""
——————————
　/Edit　/list　/setting
"""
    return final
