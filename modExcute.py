import tool, modDatabase, modSearch, modVariables
from msgMain import msgMain
from msgShort import msgShort

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
        if "/start" in self.text:
            mesut = msgMain(lingua=self.argo.lingua,tasta='start')
            if self.argo.primo == ['']:
                mesut = mesut + msgShort(lingua=self.argo.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/help" in self.text:
            mesut = msgMain(lingua=self.argo.lingua,tasta='help')
            if self.argo.primo == ['']:
                mesut = mesut + msgShort(lingua=self.argo.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/exit" in self.text:
            self.mesut = [msgShort(lingua=self.argo.lingua,tasta='bye')]
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
