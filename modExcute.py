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

    def codGen(self): #condition of general function
        resut = False
        keyse = ["/start","/help","/exit"]
        for keywo in keyse:
            if keywo in self.text:
                resut = True
        return resut

    def moGen(self):
        if "/start" in self.text:
            mesut = msgMain(lingua=self.lingua,tasta='start')
            if self.primo == ['']:
                mesut = mesut + msgShort(lingua=self.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/help" in self.text:
            mesut = msgMain(lingua=self.lingua,tasta='help')
            if self.primo == ['']:
                mesut = mesut + msgShort(lingua=self.lingua,tasta='cof')
                self.mesut = [mesut]
                self.cos=1
        elif "/exit" in self.text:
            self.mesut = [msgShort(lingua=self.lingua,tasta='bye')]
            self.cos=1

    def moRaw():
        print('')

    def __init__(self,msg,argo):
        self.text=msg['text']
        self.argo=argo

        self.mesut=[]
        self.cos=0

        self.primo = self.argo.primo
        self.submo = self.argo.submo
        self.temra = self.argo.temra
        self.keywo = self.argo.keywo
        self.kasso = self.argo.kasso

        self.lingua = self.argo.setti.get('lingua','enMY')

        if self.codGen():
            self.moGen()


        self.argo.primo = self.primo
        self.argo.submo = self.submo
        self.argo.temra = self.temra
        self.argo.keywo = self.keywo
        self.argo.kasso = self.kasso
