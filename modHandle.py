from core import tool
from core import modDatabase
from core import modVariables

import modSearch

from msgMain import MsgMain
from msgShort import MsgShort
"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from open_chat_message() in momocobot.py.
"""

class Hande:
    """ handle received msg
    pass command to excute() for futher action (which is more complex)
    change cache info that store in memory (argon)
    and reply back to user
    """
    def __init__(self,msg,argon):
        self.text = msg
        self.argo = argon

        self.resut = []
        self.cos = 0
        self.ekgu = 0

        msgMain = MsgMain(self.argo.lingua)
        primo = self.argo.database.get('mode',{})

        if max(primo.keys()) == 0 :
            self.resut = [msgMain.home({'keywo':self.text})]
            self.argo.keywo = self.text

        elif primo.get(max(primo.keys())) == 'creo':
            creodata = self.argo.database.get('creo',{})
            submo = creodata.get('submode','')
            if submo == '':
                self.resut = [msgMain.home({'keywo':self.text})]
                self.argo.keywo = self.text
                self.ekgu = 1
            elif submo == 'recom':
                self.argo.keywo = self.text
                self.ekgu = 1

        elif primo.get(max(primo.keys())) == 'saci':
            sacidata = self.argo.database.get('saci',{})
            submo = sacidata.get('submode','')
            if submo == '':
                self.resut = [msgMain.home({'keywo':self.text})]
                self.argo.keywo = self.text
                self.ekgu = 1
            elif submo == 'setio':
                self.argo.keywo = self.text
                self.ekgu = 1
