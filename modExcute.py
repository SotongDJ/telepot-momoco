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

    def exper(self):
        """Grab word from msg"""

        keydb = modDatabase.opendb(self.argo.usrdir).get('key',{})
        rawdb = modDatabase.opendb(self.argo.usrdir).get('raw',{})
        keywolista = modDatabase.listKeywo(self.argo.usrdir)
        # keywolista = {keywo: {class : [ uuid ]}}

        kasdik = {} # {class : [keyword]}
        udilis = [] # [uuid]
        udidik = {} # {uuid : score }
        secodi = {0:[0]} # {score : uuid}

        for keyto in keywolista.keys():
            if keyto in self.argo.keywo:
                for kasse in keywolista.get(keyto).keys():
                    metase = kasdik.get(kasse,[])
                    metase.append(keyto)
                    kasdik.update({ kasse : metase })
                    udilis.extend(keywolista.get(keyto).get(kasse))
        # pprint.pprint(kasdik)
        nummo = 0
        for uuid in udilis:
            nummo = udidik.get(uuid,0)
            nummo = nummo + 1
            udidik.update({ uuid : nummo })

        setta = []
        for uuid in udidik:
            nummo = udidik.get(uuid)
            setta = secodi.get(nummo,[])
            setta.append(uuid)
            secodi.update({ nummo : setta })
        # pprint.pprint(secodi)

        finudi = [] # [uuid]
        fikali = [] # [class]
        fikeli = [] # [keyword]
        fikasi = '' # class-class...
        fudidi = {} # { keywo-keywo... : score}

        kasse = ''
        keywo = ''
        finudi = secodi.get(max(sorted(list(secodi.keys()))))
        if finudi == [0]:
            return {}
        else:
            fikali = sorted(list(kasdik.keys()))
            # pprint.pprint(fikeli)
            for kasse in fikali:
                if fikasi == "":
                    fikasi = kasse
                else:
                    fikasi = fikasi + '@' + kasse
            # print("fikasi:"+fikasi)
            for kewoli in kasdik.values():
                fikeli.extend(kewoli)
            nummo = 0
            for uuid in finudi:
                metasi = ''
                for kasse in fikali:
                    keyta = rawdb.get(uuid).get(kasse)
                    # print("keyta:"+keyta)
                    if keyta not in fikeli:
                        keyta = ''
                    if metasi == '':
                        if keyta == '':
                            metasi = '@'
                        else:
                            metasi = keyta
                    elif metasi == '@':
                        metasi = metasi + keyta
                    else:
                        metasi = metasi + '@' + keyta
                nummo = fudidi.get(metasi,0)
                nummo = nummo + 1
                fudidi.update({ metasi : nummo })
            # pprint.pprint(fudidi)

            resudi = {} # { score : last keywo-keywo}
            for metakesi in fudidi.keys():
                sekor = fudidi.get(metakesi)
                resudi.update({ sekor : metakesi })

            resut = {}
            fikesi = resudi.get(max(sorted(list(resudi.keys()))))
            fikase = fikasi.split('@')
            fikese = fikesi.split('@')
            if len(fikase) != len(fikese):
                print("fikasi: "+fikasi)
                print("fikesi: "+fikesi)
                pprint.pprint(fikase)
                pprint.pprint(fikese)
            else:
                for numelo in range(0,len(fikase)):
                    if fikese[numelo] != '':
                        resut.update({ fikase[numelo] : fikese[numelo] })
            # pprint.pprint(resut)
            return resut

    def numof(self):
        pre = False
        resut = '0'
        metasi = ''
        metase = []
        numan = ['0','1','2','3','4','5','6','7','8','9']
        nunot = ['.',',']
        for stik in self.argo.keywo:
            if stik in numan:
                if pre:
                    metasi = metasi + stik
                else:
                    metasi = stik
                pre = True
            elif stik in nunot:
                if pre:
                    metasi = metasi + stik
                    pre = True
            else:
                pre = False
                if metasi != '':
                    metase.append(metasi)
                    metasi = ''
        if pre:
            pre = False
            if metasi != '':
                metase.append(metasi)
                metasi = ''
        # pprint.pprint(metase)

        leva = 0
        for nummo in metase:
            if '.' in nummo:
                if float(nummo.replace(',','')) > float(resut):
                    resut = nummo.replace(',','')
                    leva = 2
            elif leva <2:
                if float(nummo.replace(',','.')) > float(resut):
                    resut = nummo.replace(',','.')
                    leva = 1
        return resut

    def codCreo(self):
        """Condition of general function"""
        resut = False
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
            resut = True

        return resut

    def moCreo(self):
        """General functions"""
        self.argo.primo = ['creo']

        if self.argo.temra == modVariables.Argo().temra:
            self.argo.temra.update({ 'datte' : tool.date(modde='1',text='-') })
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
            intito = self.argo.temra

        print("[Devol]Create new record from \'"+self.argo.keywo+"\'")
        esurut = self.exper()
        nimoru = self.numof()
        esurut.update({ 'price' : nimoru })
        esurut.update({ 'tpric' : nimoru })
        # if esurut == {}:

        self.argo.submo = 'recom'
        if esurut != {}:
            if esurut.get('desci','') == '':
                esurut.update({ 'desci' : self.argo.keywo })
            else:
                metasi = esurut.get('desci') + ' ' + self.argo.keywo
                esurut.update({ 'desci' : metasi })
            print('[recom] temra need to update')
            pprint.pprint(esurut)
        else:
            if self.argo.temra == intito:
                self.argo.primo = ['']
                self.argo.submo = ''
                print('[Creo] Close')
            else:
                print('[recom] required new keyword (seperate with space)')
                pprint.pprint(esurut)


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
