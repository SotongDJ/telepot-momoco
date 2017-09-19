import tool, modDatabase, modSearch, modVariables
from msgMain import MsgMain
from msgShort import MsgShort

"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from comme() in momocobot.py.
"""
class Excut:
    """ process  msg
    grab command from hande()
    assign task to other mod
    and reply result back to hande()
    """

    def codGen(self):
        """Condition of general function"""
        resut = False
        keyse = ["/start","/help","/exit"]
        for keywo in keyse:
            if keywo in self.text:
                resut = True
        return resut

    def moGen(self):
        """General functions"""
        msgShort = MsgShort(self.argo.lingua)
        msgMain = MsgMain(self.argo.lingua)
        if "/start" in self.text:
            mesut = msgMain.start
            if self.argo.primo == ['']:
                mesut = mesut + msgShort.cof
                self.mesut = [mesut]
                self.cos=1
        elif "/help" in self.text:
            mesut = msgMain.help
            if self.argo.primo == ['']:
                mesut = mesut + msgShort.cof
                self.mesut = [mesut]
                self.cos=1
        elif "/exit" in self.text:
            self.mesut = [msgShort.bye]
            self.cos=1

    def moRaw(self):
        """Initial Function"""
        print('')

    def __init__(self,msg,argo):
        self.text=msg['text']
        self.argo=argo

        self.mesut=[]
        self.cos=0

        self.argo.lingua = self.argo.setti.get('lingua','enMY')

        if self.codGen():
            self.moGen()
