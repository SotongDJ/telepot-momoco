import tool, json, mmctool
#defSettMsg : main(setting), warn(), lista(setting), setup(keywo,teksi), fins(setting), discard()

""" self.sender.sendMessage(mmcmsg.setting()) """
def main(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Setting Card
----------------------------
Account:
    Default Income: """+setting['dinco']+"""
    Default Expense: """+setting['dexpe']+"""
    General Income Source: """+setting['genis']+"""
    Overall Expense Destination: """+setting['ovede']+"""

Category:
    Default Income: """+setting['tanfe']+"""
    Default Transfer: """+setting['incom']+"""

Curency:
    Default Currency: """+setting['karen']+"""
----------------------------
P.S. You still can use the last card
  /modify_Setting  /whats_now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettList(self._setting)) """
def warn():
    final="""
----------------------------
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
----------------------------
Chatbot are using G.I.S. and O.E.D for Analystic Purpose"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettList(self._setting)) """
def lista(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting Card
-------------- Account --------------
Default Income: (E.g. Bank A)
  """+setting['dinco']+""" /change_in
Default Expense: (E.g. Cash)
  """+setting['dexpe']+""" /change_ex

General Income Source:(E.g. "Income")
  """+setting['genis']+""" /change_gi
Overall Expense Destination: (E.g. "Expense")
  """+setting['ovede']+""" /change_oe

-------------- Category --------------
Default Income:(E.g. "Income")
  """+setting['incom']+""" /change_ic
Default Transfer:(E.g. "Transfer")
  """+setting['tanfe']+""" /change_tf
-------------- Curency --------------
  Default Currency: (For Expense)
  """+setting['karen']+""" /change_kr
----------------------------
    /Discard /Save /Explain
Note: Changing setting now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettSet()) """
def setup(keywo,teksi):
    final="""Select Position
----------------------------
Keyword: """+keywo+"""

Account:
    Default Income
        ( """+teksi[1][0]+"in"+teksi[1][1]+""" )
    Default Expense
        ( """+teksi[1][0]+"ex"+teksi[1][1]+""" )
    General Income Source
        ( """+teksi[1][0]+"gi"+teksi[1][1]+""" )
    Overall Expense Destination
        ( """+teksi[1][0]+"oe"+teksi[1][1]+""" )
Category:
    Default Income
      ( """+teksi[1][0]+"ic"+teksi[1][1]+""" )
    Default Transfer
      ( """+teksi[1][0]+"tf"+teksi[1][1]+""" )
Curency:
    Default Currency
      ( """+teksi[1][0]+"kr"+teksi[1][1]+""" )
----------------------------
  /Discard  /Save /Back
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettFins(self._setting))"""
def fins(setting): # will replace by Start Card after finished Account Card and Currency Card
    final="""Account Setting #Saved
----------------------------
Default Income: """+setting['dinco']+"""
Default Expense: """+setting['dexpe']+"""
General Income Source: """+setting['genis']+"""
Overall Expense Destination: """+setting['ovede']+"""

Default Income: """+setting['tanfe']+"""
Default Transfer: """+setting['incom']+"""

Default Currency: """+setting['karen']+"""
----------------------------
    /setting /Help /whats_now
Note: Changing setting now
"""
    return final

""" self.sender.sendMessage(mmcmsg.defSettDis()) """
def discard():
    final="""¡ Discard !
----------------------------

  Closed Account Setting Card

----------------------------
  /setting  /help
"""
    return final
