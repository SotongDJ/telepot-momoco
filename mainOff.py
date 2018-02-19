import auth,time

from core import tool
from core import modDatabase

import modSearch,modArgona

from modHandle import Hande
from modExcute import Excut
from msgMain import MsgMain
from msgShort import MsgShort

usrdir = 'database/usr/'+str(auth.id())
Setting = modDatabase.openSetting(usrdir=usrdir)
lingua = Setting.get('lingua','enMY')
msgMain = MsgMain(lingua)

class argo:
    def sending(self,primo='',submo='',mesag=['']):
        msgShort = MsgShort(self.lingua)
        outputes = '\n[output{'+primo+':'+submo+'}]'
        for wuerd in mesag:
            if len(wuerd) >=4069:
                parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
                for numo in range(0,len(parta)):
                    if numo == 0:
                        sentes = outputes + parta[numo] + msgShort.spitpost
                        print(sentes)
                    elif numo == len(parta) - 1:
                        sentes = outputes + msgShort.spitpre + parta[numo]
                        print(sentes)
                    else:
                        sentes = outputes + msgShort.spitpre + parta[numo]
                        sentes = sentes + msgShort.spitpost
                        print(sentes)
                    time.sleep(1)
            else:
                print(outputes + wuerd)
                time.sleep(1)

    def __init__(self):
        self.usrdir = usrdir
        self.lingua = lingua
        defal = modArgona.Argo()
        self.database = defal.database
        chatdata = self.database.get('chat')
        chatdata.update({ 'chatid' : auth.id() })
        chatdata.update({ 'content_type' : 'text' })
        self.setti = Setting
        self.veces = 0
        self.keywo = ''

condi = True
Argon = argo()
while condi:
    modde = Argon.database.get('mode',{})
    primo = modde.get(max(modde.keys()),'')
    specdata = Argon.database.get(primo,{})
    submo = specdata.get('submode','')
    testa = input('\n[input{'+ primo +':'+ submo +'}]')

    if "/" in testa:
        resul = Excut(testa,Argon)

        Argon = resul.argo
        Argon.sending(primo=primo,submo=submo,mesag=resul.mesut)
        if resul.cos == 1:
            condi = False
            print('[stop]')

    elif "/" not in testa:
        resul = Hande(testa,Argon)

        Argon = resul.argo
        Argon.sending(mesag=resul.resut)
        if resul.cos == 1:
            condi = False
            print('[stop]')
        elif resul.ekgu == 1:
            resul = Excut(testa,Argon)

            Argon = resul.argo
            Argon.sending(mesag=resul.mesut)
            if resul.cos == 1:
                condi = False
                print('[stop]')
