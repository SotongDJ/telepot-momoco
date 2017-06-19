import tool, json
import mmctool
# msgOuto : main(), keyword(), recom(), finis(), discard()

""" self.sender.sendMessage(mmcmsg.outo(self._temra)) """
def main(dicto):
    final="""New Expense Card
——————————
Date: """+dicto["datte"]+"""
Item: """+dicto["namma"]+"""
Category: """+dicto["klass"]+"""
Seller: """+dicto["shoop"]+"""
　/change_Seller
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
