import pprint

from core import tool
from core import modDatabase
from core import modSearch
from core import modVariables

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
    def bord(self):
        msgMain = MsgMain(self.argo.lingua)
        self.mesut=[msgMain.bored]

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

    def filto(self):
        resut = {}
        """Grab word from msg"""
        keywolista = modDatabase.listAll(self.argo.usrdir)
        for keyto in keywolista.keys():
            if keyto in self.argo.keywo:
                numose = list(keywolista.get(keyto).keys())
                numose.append(0)
                numose = sorted(numose)
                resut.update({ keyto : keywolista.get(keyto).get(numose[-1])[0] })
        pprint.pprint(resut)

    def codCreo(self):
        """Condition of general function"""
        resut = False
        if self.argo.primo == ['']:
            if "/new" in self.text:
                resut = True
        elif self.argo.primo == ['creo']:
            resut = True

        return resut

    def moCreo(self):
        """General functions"""
        msgMain = MsgMain(self.argo.lingua)
        self.argo.primo = ['creo']
        if self.argo.submo == '':
            print("[Devol]Create new record from \'"+self.argo.keywo+"\'")
            self.filto()

    def moRaw(self):
        """Initial Function"""
        print('')

    def __init__(self,msg,argon):
        self.text=msg
        self.argo=argon

        self.mesut=[]
        self.cos=0

        self.argo.lingua = self.argo.setti.get('lingua','SiMP')

        if self.codGen():
            self.moGen()

        elif self.codCreo():
            self.moCreo()

        else:
            self.bord()
