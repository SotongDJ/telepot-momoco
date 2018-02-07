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
        keyse = ["/start","/help","/exit","/mem"]
        for keywo in keyse:
            if keywo in self.text:
                resut = True
        return resut

    def moGen(self):
        """General functions"""
        msgShort = MsgShort(self.argo.lingua)
        msgMain = MsgMain(self.argo.lingua)
        primo = self.argo.database.get('mode',{ 0 : '' })
        if "/start" in self.text:
            messa = msgMain.start
            if max(primo.keys()) == 0:
                messa = messa + msgShort.cof
                self.mesut.append(messa)
        elif "/help" in self.text:
            messa = msgMain.help
            if max(primo.keys()) == 0:
                messa = messa + msgShort.cof
                self.mesut.append(messa)
        elif "/exit" in self.text:
            self.mesut.append(msgShort.bye)
            self.cos=1
        elif "/mem" in self.text:
            self.mesut.append(pprint.pformat(self.argo.database))

    def codCreo(self):
        """Condition of general function"""
        resut = False
        msgShort = MsgShort(self.argo.lingua)
        primo = self.argo.database.get('mode',{ 0 : '' })
        creodata = self.argo.database.get('creo',{})
        recomdata = creodata.get('recom',{})
        temradata = creodata.get('temra',{})

        if max(primo.keys()) == 0:
            if "/expense" in self.text:
                creodata.update({ 'submode' : 'expe' })
                resut = True
            elif "/transfer" in self.text:
                creodata.update({ 'submode' : 'tafe' })
                resut = True
            elif "/income" in self.text:
                creodata.update({ 'submode' : 'inco' })
                resut = True

        elif primo.get(max(primo.keys()),'') == 'creo' :
            if '/recom' in self.text:
                numano = self.text.replace('/recom','')
                metadi = recomdata.get(numano,{})
                for nan in metadi:
                    if nan != 'solok':
                        if nan == 'desci':
                            if temradata.get('desci','') == '':
                                temradata.update({ 'desci' : metadi.get('desci','') })
                            else:
                                metasi = temradata.get('desci','') + ' ' + metadi.get('desci','')
                                temradata.update({ 'desci' : metasi })
                        else:
                            temradata.update({ nan : metadi.get(nan,'') })
                creodata.update({ 'submode' : 'temra' })

            elif '/' in self.text:
                keywo = self.text[1:6]
                numano = self.text.replace('/'+keywo,'')
                if keywo in temradata.keys():
                    metadi = recomdata.get(numano,{})
                    if metadi.get(keywo,'') != '':
                        temradata.update({ keywo : metadi.get(keywo,'') })
                        if temradata.get('desci','') == '':
                            temradata.update({ 'desci' : metadi.get('desci','') })
                        else:
                            metasi = temradata.get('desci','') + ' ' + metadi.get('desci','')
                            temradata.update({ 'desci' : metasi })
                        creodata.update({ 'submode' : 'temra' })

                elif self.text[0:6] == "/temra":
                    creodata.update({ 'submode' : 'temra' })
                elif self.text[0:8] == "/discard":
                    null = primo.pop(max(primo.keys()))
                    defal = modVariables.Argo()
                    creodata = defal.database.get('creo')
                    self.argo.database.update({'creo' : creodata})
                    self.mesut.append(msgShort.empting)
                elif self.text[0:5] == "/Save":
                    if '' in temradata.values():
                        self.bos = False
                        creodata.update({ 'submode' : 'temra' })
                        self.mesut.append(msgShort.emptylist)
                    else:
                        creodata.update({ 'submode' : 'saved' })
                else:
                    self.mesut.append(msgShort.wrong)
                    creodata.update({ 'submode' : 'temra' })
            elif '/' not in self.text:
                resut = True

        return resut

    def moCreo(self):
        """General functions"""
        msgCreo = MsgCreo(lingua=self.argo.lingua)

        primo = self.argo.database.get('mode',{ 0 : '' })
        creodata = self.argo.database.get('creo',{})
        submo = creodata.get('submode','')
        recomdata = creodata.get('recom',{})
        temradata = creodata.get('temra',{})

        if primo.get(max(primo.keys()),'') != 'creo':
            temradata.update({ 'datte' : tool.date(modde=1,text='-') })
            temradata.update({ 'karen' : self.argo.setti.get('karen','') })
            temradata.update({ 'tkare' : self.argo.setti.get('karen','') })
            if submo == 'expe':
                temradata.update({ 'fromm' : self.argo.setti.get('dexpe','') })
                temradata.update({ 'toooo' : self.argo.setti.get('ovede','') })
            elif submo == 'inco':
                temradata.update({ 'fromm' : self.argo.setti.get('genis','') })
                temradata.update({ 'toooo' : self.argo.setti.get('dinco','') })
                temradata.update({ 'klass' : self.argo.setti.get('incom','') })
            elif submo == 'tafe':
                temradata.update({ 'klass' : self.argo.setti.get('tanfe','') })
            primo.update({ max(primo.keys())+1 : 'creo'})

        print("<Creo>Create new record from \'"+self.argo.keywo+"\'")
        esurut = modRecom.exper(self.argo.usrdir,self.argo.keywo)
        nimoru = modRecom.numof(self.argo.keywo)
        esurut.update({ 'price' : nimoru })
        esurut.update({ 'tpric' : nimoru })
        # if esurut == {}:
        for numak in range(0,10000):
            metanu = str(numak)
            metanu = '0'*(4-len(metanu)) + metanu
            if recomdata.get(metanu,{}).get('solok','') == '':
                numano = metanu
                break

        submo = 'recom'
        # pprint.pprint(esurut)
        if esurut != {'price':'','tpric':''}:
            if esurut.get('desci','') == '':
                esurut.update({ 'desci' : self.argo.keywo })
            else:
                metasi = esurut.get('desci') + ' ' + self.argo.keywo
                esurut.update({ 'desci' : metasi })
            print('<recom> temra need to update')
            esurut.update({ 'solok' : '@esurut@' })
            recomdata.update({ numano : esurut })
            self.mesut.append(msgCreo.recoman(esurut=esurut,numano=numano))
            esurut = {}

        else:
            print('<recom> required new keyword (seperate with space)')
            esurut = { 'solok' : '@solame@' }
            defal = modVariables.Argo()
            for n in defal.temra.keys():
                esurut.update({ n : self.argo.keywo })
            recomdata.update({ numano : esurut })
            self.mesut.append(msgCreo.recoman(esurut=esurut,numano=numano))
            esurut = {}

    def codTemra(self):
        primo = self.argo.database.get('mode',{ 0 : '' })
        creodata = self.argo.database.get('creo',{})
        submo = creodata.get('submode','')

        resut = False
        if primo.get(max(primo.keys())) == 'creo':
            if submo == 'temra':
                resut = True
        return resut

    def moTemra(self):
        creodata = self.argo.database.get('creo',{})
        temradata = creodata.get('temra',{})
        msgCreo = MsgCreo(lingua=self.argo.lingua)
        self.mesut.append(msgCreo.temran(temra=temradata))
        creodata = self.argo.database.get('creo',{})
        creodata.update({ 'submode' : 'recom' })

    def codSave(self):
        primo = self.argo.database.get('mode',{ 0 : '' })
        creodata = self.argo.database.get('creo',{})
        submo = creodata.get('submode','')

        resut = False
        if primo.get(max(primo.keys())) == 'creo':
            if submo == 'saved':
                resut = True
        return resut

    def moSave(self):
        msgCreo = MsgCreo(lingua=self.argo.lingua)
        msgShort = MsgShort(self.argo.lingua)

        primo = self.argo.database.get('mode',{})
        creodata = self.argo.database.get('creo',{})
        temradata = creodata.get('temra',{})

        modDatabase.addRaw(self.argo.usrdir,temradata)
        modDatabase.refesdb(self.argo.usrdir)
        self.mesut.append(msgShort.saved)
        self.mesut.append(msgCreo.savon(temra=temradata))

        null = primo.pop(max(primo.keys()))
        defal = modVariables.Argo()
        creodata = defal.database.get('creo')
        self.argo.database.update({'creo' : creodata})

    def codSearch(self):
        primo = self.argo.database.get('mode',{ 0 : '' })

        resut = False
        if primo.get(max(primo.keys())) == '':
            if "/search" in self.text:
                resut = True
        return resut

    def moSearch(self):
        if primo.get(max(primo.keys())) != 'sachi':
            primo.update({ max(primo.keys())+1 : 'sachi' })

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

        elif self.codSearch():
            self.moSearch()

        elif self.bos:
            self.bord()
