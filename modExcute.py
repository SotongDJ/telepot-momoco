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
        if self.argo.submo in ['']:
            print("[Devol]Create new record from \'"+self.argo.keywo+"\'")
            self.argo.temra.update(self.exper())
            pprint.pprint(self.argo.temra)

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
