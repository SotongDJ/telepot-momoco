import pprint

from core import tool
from core import modDatabase
from core import modVariables

import modSearch,modRecom

from msgMain import MsgMain
from msgShort import MsgShort
from msgCreo import MsgCreo

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
        self.mesut.append(msgMain.bored)

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
            messa = msgMain.start
            if self.argo.primo == ['']:
                messa = messa + msgShort.cof
                self.mesut.append(messa)
                self.cos=1
        elif "/help" in self.text:
            messa = msgMain.help
            if self.argo.primo == ['']:
                messa = messa + msgShort.cof
                self.mesut.append(messa)
                self.cos=1
        elif "/exit" in self.text:
            self.mesut.append(msgShort.bye)
            self.cos=1

    def codCreo(self):
        """Condition of general function"""
        resut = False
        msgShort = MsgShort(self.argo.lingua)

        if self.argo.primo == ['']:
            if "/expense" in self.text:
                self.argo.submo = 'expe'
                resut = True
            elif "/transfer" in self.text:
                self.argo.submo = 'tafe'
                resut = True
            elif "/income" in self.text:
                self.argo.submo = 'inco'
                resut = True

        elif self.argo.primo == ['creo']:
            if '/recom' in self.text:
                numano = self.text.replace('/recom','')
                metadi = self.argo.recom.get(numano,{})
                for nan in metadi:
                    if nan != 'solok':
                        if nan == 'desci':
                            if self.argo.temra.get('desci','') == '':
                                self.argo.temra.update({ 'desci' : metadi.get('desci','') })
                            else:
                                metasi = self.argo.temra.get('desci','') + ' ' + metadi.get('desci','')
                                self.argo.temra.update({ 'desci' : metasi })
                        else:
                            self.argo.temra.update({ nan : metadi.get(nan,'') })
                self.argo.submo = 'temra'

            elif '/' in self.text:
                keywo = self.text[1:6]
                numano = self.text.replace('/'+keywo,'')
                if keywo in self.argo.temra.keys():
                    metadi = self.argo.recom.get(numano,{})
                    if metadi.get(keywo,'') != '':
                        self.argo.temra.update({ keywo : metadi.get(keywo,'') })
                        if self.argo.temra.get('desci','') == '':
                            self.argo.temra.update({ 'desci' : metadi.get('desci','') })
                        else:
                            metasi = self.argo.temra.get('desci','') + ' ' + metadi.get('desci','')
                            self.argo.temra.update({ 'desci' : metasi })
                        self.argo.submo = 'temra'

                elif self.text[0:6] == "/temra":
                    self.argo.submo = 'temra'
                elif self.text[0:8] == "/discard":
                    self.argo.primo = ['']
                    self.argo.submo = ''
                    self.argo.temra = {}
                    self.argo.recom = {}
                    self.mesut.append(msgShort.empting)
                elif self.text[0:5] == "/Save":
                    if '' in self.argo.temra.values():
                        self.bos = False
                        self.argo.submo = 'temra'
                        self.mesut.append(msgShort.emptylist)
                    else:
                        self.argo.submo = 'saved'
                else:
                    self.mesut.append(msgShort.wrong)
                    self.argo.submo = 'temra'
            elif '/' not in self.text:
                resut = True

        return resut

    def moCreo(self):
        """General functions"""
        msgCreo = MsgCreo(lingua=self.argo.lingua)
        if self.argo.primo != ['creo']:
            self.argo.temra.update({ 'datte' : tool.date(modde=1,text='-') })
            self.argo.temra.update({ 'karen' : self.argo.setti.get('karen','') })
            self.argo.temra.update({ 'tkare' : self.argo.setti.get('karen','') })
            if self.argo.submo == 'expe':
                self.argo.temra.update({ 'fromm' : self.argo.setti.get('dexpe','') })
                self.argo.temra.update({ 'toooo' : self.argo.setti.get('ovede','') })
            elif self.argo.submo == 'inco':
                self.argo.temra.update({ 'fromm' : self.argo.setti.get('genis','') })
                self.argo.temra.update({ 'toooo' : self.argo.setti.get('dinco','') })
                self.argo.temra.update({ 'klass' : self.argo.setti.get('incom','') })
            elif self.argo.submo == 'tafe':
                self.argo.temra.update({ 'klass' : self.argo.setti.get('tanfe','') })
        self.argo.primo = ['creo']

        print("<Creo>Create new record from \'"+self.argo.keywo+"\'")
        esurut = modRecom.exper(self.argo.usrdir,self.argo.keywo)
        nimoru = modRecom.numof(self.argo.keywo))
        esurut.update({ 'price' : nimoru })
        esurut.update({ 'tpric' : nimoru })
        # if esurut == {}:
        for numak in range(0,10000):
            metanu = str(numak)
            metanu = '0'*(4-len(metanu)) + metanu
            if self.argo.recom.get(metanu,{}).get('solok','') == '':
                numano = metanu
                break

        self.argo.submo = 'recom'
        # pprint.pprint(esurut)
        if esurut != {'price':'','tpric':''}:
            if esurut.get('desci','') == '':
                esurut.update({ 'desci' : self.argo.keywo })
            else:
                metasi = esurut.get('desci') + ' ' + self.argo.keywo
                esurut.update({ 'desci' : metasi })
            print('<recom> temra need to update')
            esurut.update({ 'solok' : '@esurut@' })
            self.argo.recom.update({ numano : esurut })
            self.mesut.append(msgCreo.recoman(esurut=esurut,numano=numano))
            esurut = {}

        else:
            print('<recom> required new keyword (seperate with space)')
            esurut = { 'solok' : '@solame@' }
            defal = modVariables.Argo()
            for n in defal.temra.keys():
                esurut.update({ n : self.argo.keywo })
            self.argo.recom.update({ numano : esurut })
            self.mesut.append(msgCreo.recoman(esurut=esurut,numano=numano))
            esurut = {}

    def codTemra(self):
        resut = False
        if self.argo.primo == ['creo']:
            if self.argo.submo == 'temra':
                resut = True
        return resut

    def moTemra(self):
        msgCreo = MsgCreo(lingua=self.argo.lingua)
        self.mesut.append(msgCreo.temran(temra=self.argo.temra))
        self.argo.submo = 'recom'

    def codSave(self):
        resut = False
        if self.argo.primo == ['creo']:
            if self.argo.submo == 'saved':
                resut = True
        return resut

    def moSave(self):
        msgCreo = MsgCreo(lingua=self.argo.lingua)
        msgShort = MsgShort(self.argo.lingua)

        modDatabase.addRaw(self.argo.usrdir,self.argo.temra)
        modDatabase.refesdb(self.argo.usrdir)
        self.mesut.append(msgShort.saved)
        self.mesut.append(msgCreo.savon(temra=self.argo.temra))

        self.argo.primo = ['']
        self.argo.submo = ''
        self.argo.temra = {}
        self.argo.recom = {}

    def codSearch(self):
        resut = False
        if self.argo.primo == ['']:
            if "/search" in self.text:
                self.argo.submo = 'expe'
                resut = True
        return resut

    def moSearch(self):
        self.mesut = ['HaHa']
        
    def __init__(self,msg,argon):
        self.text=msg
        self.argo=argon

        self.mesut=[]
        self.cos=0

        self.bos = True

        self.argo.lingua = self.argo.setti.get('lingua','SiMP')

        if self.codGen():
            self.moGen()

        elif self.codCreo():
            self.moCreo()

        elif self.codTemra():
            self.moTemra()

        elif self.codSave():
            self.moSave()

        elif self.bos:
            self.bord()
