class MsgSetti:
    def main(self,setti): # will replace by Start Card after finished Account Card and Currency Card
        if self.lingua == "enMY":
            final = """Setting Card
——————————
Account:
　Default Income: """+setti.get('dinco',"____")+"""
　Default Expense: """+setti.get('dexpe',"____")+"""
　General Income Source: """+setti.get('genis',"____")+"""
　Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Category:
　Default Income: """+setti.get('tanfe',"____")+"""
　Default Transfer: """+setti.get('incom',"____")+"""
　　　——————　　
Curency:
　Default Currency: """+setti.get('karen',"____")+"""
　　　——————　　
Language:
　Default Language: """+setti.get('lingua',"____")+"""
——————————
　/modify_Setting　/whats_now
Remind:
　Use whats_now to check status of current work
"""
            return final

    elif self.lingua == "hanT":
            final = """Setting Card
——————————
Account:
　Default Income: """+setti.get('dinco',"____")+"""
　Default Expense: """+setti.get('dexpe',"____")+"""
　General Income Source: """+setti.get('genis',"____")+"""
　Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Category:
　Default Income: """+setti.get('tanfe',"____")+"""
　Default Transfer: """+setti.get('incom',"____")+"""
　　　——————　　
Curency:
　Default Currency: """+setti.get('karen',"____")+"""
　　　——————　　
Language:
　Default Language: """+setti.get('lingua',"____")+"""
——————————
　/modify_Setting　/whats_now
Remind:
　Use whats_now to check status of current work
"""
            return final

""" self.sender.sendMessage(mmcmsg.defSettList(self._setting)) """
def warn():
    final="""
——————————
Normal Income:
　G.I.S. ---> Bank A , Category: Income
Normal Expense:
　Cash ---> O.E.D. , Category: Expense
Withdrawal:
　Bank A ---> Cash , Category: Transfer
Deposit:
　Cash ---> Bank A , Category: Transfer
Tranfer:
　Bank A ---> Bank B , Category: Transfer
——————————
Notes:
　Chatbot are using G.I.S. and O.E.D. for Analystic Purpose
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettList(self._setting)) """
def lista(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting Card
————— Account —————
Default Income: (E.g. Bank A)
　"""+setti.get('dinco',"____")+"""　/change_in
Default Expense: (E.g. Cash)
　"""+setti.get('dexpe',"____")+"""　/change_ex
　　——————　　
General Income Source:(E.g. "Income")
　"""+setti.get('genis',"____")+"""　/change_gi
Overall Expense Destination: (E.g. "Expense")
　"""+setti.get('ovede',"____")+"""　/change_oe
————— Category —————
Default Income:(E.g. "Income")
　"""+setti.get('incom',"____")+"""　/change_ic
Default Transfer:(E.g. "Transfer")
　"""+setti.get('tanfe',"____")+"""　/change_tf
————— Curency —————
Default Currency: (For Expense)
　"""+setti.get('karen',"____")+"""　/change_kr
————— Curency —————
Default Language:
　"""+setti.get('lingua',"____")+"""　/change_lingua
——————————
　/Discard　/Save　/Explain
Note:
　Changing setting now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettSet()) """
def setup(keywo,teksi):
    final="""Select Position
——————————
Keyword: """+keywo+"""
　　——————　　
Account:
　Default Income
　( """+teksi[1][0]+"in"+teksi[1][1]+""" )
　Default Expense
　( """+teksi[1][0]+"ex"+teksi[1][1]+""" )
　General Income Source
　( """+teksi[1][0]+"gi"+teksi[1][1]+""" )
　Overall Expense Destination
　( """+teksi[1][0]+"oe"+teksi[1][1]+""" )
　　——————　　
Category:
　Default Income
　( """+teksi[1][0]+"ic"+teksi[1][1]+""" )
　Default Transfer
　( """+teksi[1][0]+"tf"+teksi[1][1]+""" )
　　——————　　
Curency:
　Default Currency
　( """+teksi[1][0]+"kr"+teksi[1][1]+""" )
——————————
　/Discard　/Save　/Back
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettFins(self._setting))"""
def fins(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting #Saved
——————————
Default Income: """+setti.get('dinco',"____")+"""
Default Expense: """+setti.get('dexpe',"____")+"""
General Income Source: """+setti.get('genis',"____")+"""
Overall Expense Destination: """+setti.get('ovede',"____")+"""
　　——————　　
Default Income: """+setti.get('tanfe',"____")+"""
Default Transfer: """+setti.get('incom',"____")+"""
　　——————　　
Default Currency: """+setti.get('karen',"____")+"""
　　——————　　
Default Language: """+setti.get('lingua',"____")+"""
——————————
　/setting　/help　/whats_now
Note:
　Changing setting now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettDis()) """
def discard():
    final="""¡ Discard !
——————————

　Closed Account Setting Card

——————————
　/whats_now　/setting　/help
"""
    return final
