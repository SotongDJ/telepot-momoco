import auth,time

from core import tool
from core import modDatabase
from core import modSearch
from core import modVariables

from modHandle import Hande
from modExcute import Excut
from msgMain import MsgMain
from msgShort import MsgShort

usrdir = 'database/usr/'+str(auth.id())
Setting = modDatabase.openSetting(usrdir=usrdir)
lingua = Setting.get('lingua','enMY')
msgMain = MsgMain(lingua)
defal = modVariables.Argo()

class argo:
    def sending(self,mesag=['']):
        msgShort = MsgShort(self.lingua)
        for wuerd in mesag:
            if len(wuerd) >=4069:
                parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
                for numo in range(0,len(parta)):
                    if numo == 0:
                        sentes = '[output]' + parta[numo] + msgShort.spitpost
                        print(sentes)
                    elif numo == len(parta) - 1:
                        sentes = '[output]' + msgShort.spitpre + parta[numo]
                        print(sentes)
                    else:
                        sentes = '[output]' + msgShort.spitpre + parta[numo]
                        sentes = sentes + msgShort.spitpost
                        print(sentes)
                    time.sleep(1)
            else:
                print('[output]' + wuerd)
                time.sleep(1)

    def __init__(self):
        self.usrdir = usrdir
        self.lingua = lingua
        self.catid = auth.id()
        self.cotyp = 'text'
        self.primo = ['']
        self.submo = ''
        self.setti = Setting
        self.veces = 0
        self.keywo = ''
        self.temra = defal.temra

condi = True
Argon = argo()
while condi:
    testa = input('[input{'+Argon.primo[-1]+'}]')

    if "/" in testa:
        resul = Excut(testa,Argon)

        Argon.sending(mesag=resul.mesut)
        Argon = resul.argo
        if resul.cos == 1:
            condi = False
            print('[stop]')

    elif "/" not in testa:
        resul = Hande(testa,Argon)

        Argon.sending(mesag=resul.resut)
        Argon = resul.argo
        if resul.cos == 1:
            condi = False
            print('[stop]')
        elif resul.ekgu == 1:
            resul = Excut(testa,Argon)

            Argon.sending(mesag=resul.mesut)
            Argon = resul.argo
            if resul.cos == 1:
                condi = False
                print('[stop]')