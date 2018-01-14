import sys, os, traceback, telepot, time, json, random, pprint
import tool, auth, log, mmctool, mmcdb, mmcDefauV, mmcAnali, mmcSachi
from libmsgMmc import msgMain, mainShort, msgCreo, msgOuto, msgInco, msgTran
from libmsgMmc import msgDefSet, msgList, msgEdit, msgAnali, msgSachi
from telepot.delegate import per_chat_id, create_open, pave_event_space

"""Command list
help - Show command list
whats_now - Show current unsaved work
new - Create new record
list - Show prevous record
statics - View statistics card
start - Welcome and Introduction
setting - View setting card
exit - Close conversation
"""

class User(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self._vez = 0
        self._keywo = ""
        self._keys = ""
        self._mod = ['']
        self._sumo = ''
        self._temra = mmcDefauV.keywo('temra')
        self._recom = {}
        self._defSett = {}
        self._statics = mmcDefauV.keywo('statics')
        self._list = mmcDefauV.keywo('list')
        self._setting = mmcDefauV.keywo('setting')
        self._karatio = {}
        self._rawdb = {}
        self._keydb = {}
    #
    def printbug(self,text,usrid):
        filla = open(tool.path('log/mmcbot',usrid=auth.id())+tool.date(modde=5),'a')
        print("---"+text+"---")
        filla.write('\n--- pri: ' + text + '---\n')
        filla.write('Time: ' + tool.date(modde=2) + '\n')
        filla.write('User: ' + str(auth.id()) + '\n')
        filla.write('keywo: ' + pprint.pformat(self._keywo) + '\n')
        filla.write('keys: ' + pprint.pformat(self._keys) + '\n')
        filla.write('mod: ' + pprint.pformat(self._mod) + '\n')
        filla.write('temra: ' + pprint.pformat(self._temra) + '\n')
        filla.write('recom: ' + pprint.pformat(self._recom) + '\n')
        filla.write('defSett: ' + pprint.pformat(self._defSett) + '\n')
        filla.write('setting: ' + pprint.pformat(self._setting) + '\n')
        filla.write('--- pri fin ---\n')
        filla.close()

    def sending(self,wuerd,modda=0):
        lingua = self._setting['lingua']
        if len(wuerd) >=4069:
            parta = [ wuerd[i:i+4000] for i in range(0, len(wuerd), 4000) ]
            for numo in range(0,len(parta)):
                if numo == 0:
                    self.sender.sendMessage(parta[numo]+mainShort.woood(lingua,'spitpost'))
                elif numo == len(parta) - 1:
                    self.sender.sendMessage(mainShort.woood(lingua,'spitpre')+parta[numo])
                else:
                    self.sender.sendMessage(mainShort.woood(lingua,'spitpre')+parta[numo]+mainShort.woood(lingua,'spitpost'))

                if modda == 1:
                    self._vez=mmctool.finvez(self._vez)
                else:
                    self._vez=mmctool.printvez(self._vez)

                time.sleep(1)
        else:
            self.sender.sendMessage(wuerd)

            if modda == 1:
                self._vez=mmctool.finvez(self._vez)
            else:
                self._vez=mmctool.printvez(self._vez)

            time.sleep(1)

    def stacksend(self,staak,modda=0):
        lingua = self._setting['lingua']
        for wuerd in staak:
            sending(wuerd)

        if modda == 1:
            self._vez=mmctool.finvez(self._vez)

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        lingua = self._setting['lingua']
        if "/start" in text:
            if self._mod[-1] == '':
                tasStart=msgMain.start()+mainShort.woood(lingua,'cof')
                finno = 1
            else:
                tasStart=msgMain.start()
                finno = 0

            self.sending(tasStart, modda = finno )

            if self._mod[-1] == '':
                self.close()

        elif "/help" in text:
            if self._mod[-1] == '':
                tasHelp=msgMain.help()+mainShort.woood(lingua,'cof')
                finno = 1
            else:
                tasHelp=msgMain.help()
                finno = 0

            self.sending(tasHelp, modda = finno )

            if self._mod[-1] == '':
                self.close()

        elif "/setting" in text:
            self.sending(msgDefSet.main(self._setting))

        elif "/modify_Setting" in text:
            self.sending(mainShort.woood(lingua,'refeson'))
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            if self._mod[-1] == '':
                self._mod=mmctool.apmod(self._mod,'defSett')
            else:
                if self._mod[-1] != 'defSett':
                    self._mod=mmctool.apmod(self._mod,'defSett')

            tasDeSet=mainShort.woood(lingua,'refesfin')+msgDefSet.lista(self._setting)
            self.sending(tasDeSet)

            if self._setting['defSettWarn'] == 0:
                self.sending(msgDefSet.warn())
                self._setting['defSettWarn'] = 1
                mmcdb.changeSetting(self._setting,chat_id)

        elif "/exit" in text:
            self.sending(mainShort.woood(lingua,'bye') , modda = 1)
            self.close()

        elif "/new" in text:
            self.sending(mainShort.woood(lingua,'refeson'))
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            if self._mod[-1] == '':
                self._temra["datte"] = tool.date(modde=1)
                self._temra['fromm'] = self._setting['dexpe']
                self._temra['toooo'] = self._setting['ovede']
                self._temra['karen'] = self._setting['karen']
                self._temra['tkare'] = self._setting['karen']

                self._sumo = 'outo'

            if self._keywo != "":
                if '/' not in self._keywo:
                    tasOut = mainShort.woood(lingua,'refesfin') + msgCreo.keyword(self._keywo)
                    self.sending(tasOut)
            else:
                tasOut=mainShort.woood(lingua,'refesfin')+msgOuto.main(self._temra)+mainShort.woood(lingua,'rekeswd')
                self.sending(tasOut)

            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod( self._mod,'creo' )

        elif "/list" in text:
            self.sending(mainShort.woood(lingua,'refeson'))
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            self._sumo = ''
            if self._mod[-1] == '':
                lastdate = list(self._keydb['datte'])
                lastdate.sort()
                try:
                    self._list.update({ 'datte' : lastdate[-1] })
                except IndexError :
                    self._list.update({ 'datte' : '' })
            tasList=mainShort.woood(lingua,'refesfin')+msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id))
            self.sending(tasList)
            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod(self._mod,"list")

        elif "/Edit" in text:
            if self._mod[-1] == "list":
                uuid = self._list.get('uuid','')
                if uuid !='':
                    self._mod = mmctool.apmod(self._mod,'edit')
                    self._keywo = ''
                    self._temra.update(self._rawdb.get(uuid,''))
                    self.sending(msgEdit.main(self._temra,uuid)+mainShort.woood(lingua,'rekeswd'))
                    self._vez = mmctool.printvez(self._vez)
                else:
                    self.sending(msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                    self._vez = mmctool.printvez(self._vez)
            else:
                self.sending(msgMain.keywo('whatsnow'))
                self._vez = mmctool.printvez(self._vez)

        elif "/statics" in text:
            self.sending(mainShort.woood(lingua,'refeson'))
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            self._sumo = ''
            tasPoce=mainShort.woood(lingua,'refesfin')
            resKa = mmcdb.getKaratio(self._keydb)
            if resKa:
                tasPoce=tasPoce+mainShort.woood(lingua,'refka')
                self.sending(tasPoce)
                tasPoce=''
            else:
                tasPoce = tasPoce+mainShort.woood(lingua,'kaDatte')+tool.acedate('momoco','karen')
                tasPoce = tasPoce+mainShort.woood(lingua,'cband')
            self._karatio = mmcdb.openKaratio()
            tasList=tasPoce+msgAnali.chooseMode(lingua)
            self.sending(tasList)
            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod(self._mod,"statics")

        elif self._mod[-1] == '':
            self.sending(msgMain.bored()+mainShort.woood(lingua,'cof') , modda = 1)
            self.close()

        elif self._mod[-1] == "list":
            if self._sumo == 'sachi':
                if "/Back" in text:
                    self._sumo = ''
                    self._list.update({'uuid' : '' })
                    self.sending(msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))

                elif "/Search" in text:
                    self._statics.update({ 'mode' : 'sachi' })
                    if mmcAnali.check(self._statics):
                        self.sending(mainShort.woood(lingua,'analiWarn'))
                    else:
                        self._sumo = ''
                        melib = mmcSachi.sachi(chat_id,self._statics)
                        tasta = mmcSachi.listSachi(chat_id,melib)
                        self.sending(msgList.main(lingua,' - ',tasta))

                elif '/change_cokas' in text:
                    skdic = mmcDefauV.keywo('transle')
                    keywo = 'cokas'
                    titil = skdic.get(keywo,'')
                    self.sending(msgMain.selection(mmcAnali.listClass(keywo,lingua=lingua),titil))

                elif '/set_cokas_as_' in text:
                    self._statics.update({ 'cokas' : text.replace('/set_cokas_as_','') })
                    self.sending(msgSachi.listMain(lingua,self._statics))

                elif '/set_as_' in text:
                    if '/set_as_btempo' in text:
                        self._statics.update({ 'btempo' : self._keywo })
                    elif '/set_as_ftempo' in text:
                        self._statics.update({ 'ftempo' : self._keywo })
                    elif '/set_as_keywo' in text:
                        self._statics.update({ 'keywo' : self._keywo })

                    self.sending(msgSachi.listMain(lingua,self._statics))

            else:
                if "/Back" in text:
                    self._list.update({'uuid' : '' })
                    self.sending(msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))

                elif "/Search" in text:
                    self._sumo = 'sachi'
                    self.sending(msgSachi.listMain(lingua,self._statics))

            if "/whats_now" in text:
                self.sending(msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))

            elif "/Close" in text:
                self.sending(msgList.disca(lingua)+mainShort.woood(lingua,'cof') , modda = 1)
                self._mod=[]
                self.close()

            elif "/uuid_" in text:
                print('uuid')
                for sette in text.split(' '):
                    if "/uuid_" in sette:
                        self._list.update({'uuid' : sette.replace('/uuid_','') })
                        self.sending(msgList.single(lingua,self._list.get('uuid',''),chat_id,self._rawdb))

            elif "/Choose_" in text:
                for sette in text.split(' '):
                    if "/Choose_" in sette:
                        keywo = sette.replace("/Choose_",'').replace('_','-')
                setta = mmctool.filteDate(list(self._keydb['datte']),keywo)
                testa = mmctool.cmdzDate(setta)
                self.sending(msgList.change(lingua,keywo,testa))

            elif "/ch_" in text:
                self._sumo = ''
                tasta = ''
                for takso in text.split(' '):
                    if '/ch_' in takso:
                        tasta = takso.replace('/ch_','').replace('_','-')
                self._list.update({'datte' : tasta })
                self.sending(msgList.main(lingua,self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))

        elif self._mod[-1] == "statics":
            if "/Analysis" in text:
                if self._statics['mode'] != '':
                    print('statics : '+pprint.pformat(self._statics, compact=True))

                    if mmcAnali.check(self._statics):
                        self.sending(mainShort.woood(lingua,'analiWarn'))
                    else:
                        if self._statics['mode'] == 'abratio':
                            medio = mmcAnali.abratio(chat_id,self._statics)
                            secto = msgAnali.abratioResut(lingua,medio)
                        elif self._statics['mode'] == 'atren':
                            medio = mmcAnali.atren(chat_id,self._statics)
                            secto = msgAnali.atrenResut(lingua,medio)
                        elif self._statics['mode'] == 'akaun':
                            medio = mmcAnali.akaun(chat_id,self._statics)
                            secto = msgAnali.akaunResut(lingua,medio)
                        for lun in secto:
                            self.sending(lun)
                else:
                    self.sending(msgMain.keywo('whatsnow'))

            elif "/whats_now" in text:
                self.sending(msgMain.keywo('whatsnow'))

            elif "/Back" in text:
                if self._statics['mode'] != '':
                    if self._statics['mode'] == 'abratio':
                        self.sending(msgAnali.chooseMode(lingua))
                        self._statics['mode'] = ''
                    elif self._statics['mode'] == 'atren':
                        self.sending(msgAnali.chooseMode(lingua))
                        self._statics['mode'] = ''
                    elif self._statics['mode'] == 'akaun':
                        self.sending(msgAnali.chooseMode(lingua))
                        self._statics['mode'] = ''
                else:
                    self._statics = mmcDefauV.keywo('statics')
                    self.sending(msgAnali.chooseMode(lingua))

            elif "/Close" in text:
                self.sending(msgAnali.disca(lingua)+mainShort.woood(lingua,'cof') , modda = 1 )
                self._mod=[]
                self.close()

            elif "/Discard" in text:
                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenMain(lingua,self._statics))
                elif self._statics['mode'] == 'akaun':
                    self.sending(msgAnali.akaunMain(lingua,self._statics))

            elif '/set_Mode_as_' in text:
                if '/set_Mode_as_abratio' in text:
                    self._statics['mode'] = 'abratio'
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif '/set_Mode_as_atren' in text:
                    self._statics['mode'] = 'atren'
                    self.sending(msgAnali.atrenMain(lingua,self._statics))
                elif '/set_Mode_as_akaun' in text:
                    self._statics['mode'] = 'akaun'
                    self.sending(msgAnali.akaunMain(lingua,self._statics))

            elif '/change_acuno' in text:
                self._recom = mmcdb.listAcc('ch','chs','acuno',chat_id)
                self.sending(msgMain.selection(self._recom[1],mmcDefauV.keywo('transle',lingua=lingua).get('acuno','acuno')))

            elif '/change_' in text:
                skdic = mmcDefauV.keywo('transle')
                if '/change_cokas' in text:
                    keywo = 'cokas'
                elif '/change_targe' in text:
                    keywo = 'targe'
                titil = skdic.get(keywo,'')
                self.sending(msgMain.selection(mmcAnali.listClass(keywo,lingua=lingua),titil))

            elif '/set_cokas_as_' in text:
                self._statics.update({ 'cokas' : text.replace('/set_cokas_as_','') })
                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenMain(lingua,self._statics))
                elif self._statics['mode'] == 'akaun':
                    self.sending(msgAnali.akaunMain(lingua,self._statics))

            elif '/set_targe_as_' in text:
                self._statics.update({ 'targe' : text.replace('/set_targe_as_','') })
                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenMain(lingua,self._statics))

            elif '/set_Leve_in_' in text:
                if '/set_Leve_in_Day' in text:
                    self._statics.update({ 'leve' : 10 })
                elif '/set_Leve_in_Month' in text:
                    self._statics.update({ 'leve' : 7 })
                elif '/set_Leve_in_Year' in text:
                    self._statics.update({ 'leve' : 4 })

                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenMain(lingua,self._statics))

            elif '/set_as_' in text:
                if '/set_as_btempo' in text:
                    self._statics.update({ 'btempo' : self._keywo })
                elif '/set_as_ftempo' in text:
                    self._statics.update({ 'ftempo' : self._keywo })
                elif '/set_as_cokey' in text:
                    self._statics.update({ 'cokey' : self._keywo })
                elif '/set_as_targe' in text:
                    self._statics.update({ 'targe' : self._keywo })
                elif '/set_as_balan' in text:
                    self._statics.update({ 'balan' : self._keywo })

                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioMain(lingua,self._statics))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenMain(lingua,self._statics))
                elif self._statics['mode'] == 'akaun':
                    self.sending(msgAnali.akaunMain(lingua,self._statics))

            elif "/ch" in text :
                for sette in text.split(" "):
                    if "/chs_" in sette:
                        try:
                            wahfu = sette.split('_')
                            self._keys = wahfu[1]
                            self._keywo = self._recom[2][wahfu[2]]
                            self._statics.update({ self._keys : self._keywo })

                            if self._statics['mode'] == 'akaun':
                                self.sending(msgAnali.akaunMain(lingua,self._statics))

                        except KeyError:
                            print("KeyError : Doesn't Exist or Expired")

                            if self._statics['mode'] == 'akaun':
                                self.sending(mainShort.woood(lingua,'rgsWarn')+msgAnali.akaunMain(lingua,self._statics)+mainShort.woood(lingua,'rekeswd'))

                    elif "/ch_" in sette:
                        self._statics.update({ wahfu[1] : wahfu[2] })
                        if self._statics['mode'] == 'akaun':
                            self.sending(msgAnali.akaunMain(lingua,self._statics))

        elif self._mod[-1] in ['creo','edit']:
            if "/Discard" in text:
                self._keywo = ''
                for key in self._temra.keys():
                    self._temra.update({ key : '' })

                if self._mod[-1] == 'edit':
                    mmctool.printbug("Discard editing\n mod",self._mod,chat_id)
                    self.sending(msgEdit.discar()+mainShort.woood(lingua,'cof'))
                else:
                    mmctool.printbug("Discard record\n mod",self._mod,chat_id)
                    self.sending(msgCreo.discard()+mainShort.woood(lingua,'cof') , modda = 1)

                self._mod=mmctool.popmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

                if self._mod[-1] != 'edit':
                    self.close()

            elif "/Save" in text:
                if self._mod[-1] == 'edit':
                    uuid = self._list.get('uuid','')
                    record = mmcdb.chRaw(self._temra,uuid,chat_id)
                elif self._sumo == 'inco':
                    self._temra['price'] = self._temra['tpric']
                    self._temra['karen'] = self._temra['tkare']
                    self._temra['fromm'] = self._setting['genis']
                    record = mmcdb.addRaw(chat_id,self._temra)
                elif self._sumo == 'outo':
                    self._temra['tpric'] = self._temra['price']
                    self._temra['tkare'] = self._temra['karen']
                    self._temra['toooo'] = self._setting['ovede']
                    record = mmcdb.addRaw(chat_id,self._temra)
                else:
                    record = mmcdb.addRaw(chat_id,self._temra)

                if self._sumo == 'outo':
                    self.sending(msgOuto.finis(self._temra)+mainShort.woood(lingua,'cof') , modda = 1)
                elif self._sumo == 'inco':
                    self.sending(msgInco.finis(self._temra)+mainShort.woood(lingua,'cof') , modda = 1)
                elif self._sumo == 'tran':
                    self.sending(msgTran.finis(self._temra)+mainShort.woood(lingua,'cof') , modda = 1)
                elif self._mod[-1] == 'edit':
                    self.sending(msgEdit.fin(uuid,chat_id,record)+mainShort.woood(lingua,'cof'))

                if self._mod[-1] == 'edit':
                    self._mod=mmctool.popmod(self._mod)
                    mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)
                else:
                    self.close()

            elif "/set_as" in text :
                self._keywo = self._keywo.replace(" ","_")
                if "/set_as_Date" in text:
                    self._temra.update({ 'datte' : self._keywo })
                    self._keys='datte'
                elif "/set_as_Item" in text:
                    self._temra.update({ 'namma' : self._keywo })
                    self._keys='namma'
                elif "/set_as_Remind" in text:
                    self._temra.update({ 'namma' : self._keywo })
                    self._keys='namma'
                elif "/set_as_Category" in text:
                    self._temra.update({ 'klass' : self._keywo })
                    self._keys='klass'
                elif "/set_as_Seller" in text:
                    self._temra.update({ 'shoop' : self._keywo })
                    self._keys='shoop'
                elif "/set_as_Agent" in text:
                    self._temra.update({ 'shoop' : self._keywo })
                    self._keys='shoop'
                elif "/set_as_Account_From" in text:
                    self._temra.update({ 'fromm' : self._keywo })
                    self._keys='fromm'
                elif "/set_as_Account_To" in text:
                    self._temra.update({ 'toooo' : self._keywo })
                    self._keys='toooo'
                elif "/set_as_Account" in text:
                    self._temra.update({ 'fromm' : self._keywo })
                    self._keys='fromm'
                elif "/set_as_Price" in text:
                    self._temra.update({ 'price' : self._keywo })
                    self._keys='price'
                elif "/set_as_Notes" in text:
                    self._temra.update({ 'desci' : self._keywo })
                    self._keys='desci'
                elif "/set_as_Income" in text:
                    self._temra.update({ 'tpric' : self._keywo })
                    self._keys='tpric'
                elif "/set_as_Amount_From" in text:
                    self._temra.update({ 'price' : self._keywo })
                    self._keys='price'
                elif "/set_as_Amount_To" in text:
                    self._temra.update({ 'tpric' : self._keywo })
                    self._keys='tpric'
                elif "/set_as_Currency_Source" in text:
                    self._temra.update({ 'karen' : self._keywo })
                    self._keys='karen'
                elif "/set_as_Currency_Target" in text:
                    self._temra.update({ 'tkare' : self._keywo })
                    self._keys='tkare'
                elif "/set_as_Currency" in text:
                    self._temra.update({ 'karen' : self._keywo })
                    self._keys='karen'
                tasRef=''
                if self._sumo == 'outo':
                    tasRef=msgOuto.main(self._temra)
                elif self._sumo == 'inco':
                    tasRef=msgInco.main(self._temra)
                elif self._sumo == 'tran':
                    tasRef=msgTran.main(self._temra)
                elif self._mod[-1] == 'edit':
                    tasRef=msgEdit.main(self._temra,self._list.get('uuid',''))

                if self._keys in mmcDefauV.keywo('recset'):
                    self._recom = mmcdb.recomtxt(self._temra,self._recom,self._keys,self._keywo,mmcDefauV.keywo('recset'),chat_id)
                    if self._recom[1] !="" :
                        self.sending(tasRef)
                        self.sending(msgCreo.recom(self._recom[1],self._keywo))
                    else:
                        self.sending(tasRef+mainShort.woood(lingua,'rekeswd'))
                else:
                    self.sending(tasRef+mainShort.woood(lingua,'rekeswd'))

            elif "/rg" in text :
                for sette in text.split(" "):
                    if "/rgs_" in sette:
                        try:
                            self._keys = mmcDefauV.keywo('sf')[sette[5:7]]
                            self._keywo = self._recom[2][sette[8:len(sette)]]
                            self._temra.update({ self._keys : self._keywo })

                            if self._sumo == 'outo':
                                tasRg=msgOuto.main(self._temra)
                            elif self._sumo == 'inco':
                                tasRg=msgInco.main(self._temra)
                            elif self._sumo == 'tran':
                                tasRg=msgTran.main(self._temra)
                            elif self._mod[-1] == 'edit':
                                tasRg=msgEdit.main(self._temra,self._list.get('uuid',''))

                        except KeyError:
                            print("KeyError : Doesn't Exist or Expired")

                            if self._sumo == 'outo':
                                tasRg=mainShort.woood(lingua,'rgsWarn')+msgOuto.main(self._temra)+mainShort.woood(lingua,'rekeswd')
                            elif self._sumo == 'inco':
                                tasRg=mainShort.woood(lingua,'rgsWarn')+msgInco.main(self._temra)+mainShort.woood(lingua,'rekeswd')
                            elif self._sumo == 'tran':
                                tasRg=mainShort.woood(lingua,'rgsWarn')+msgTran.main(self._temra)+mainShort.woood(lingua,'rekeswd')
                            elif self._mod[-1] == 'edit':
                                tasRg=mainShort.woood(lingua,'rgsWarn')+msgEdit.main(self._temra,self._list.get('uuid',''))+mainShort.woood(lingua,'rekeswd')

                        if self._keys in mmcDefauV.keywo('recset'):
                            self._recom = mmcdb.recomtxt(self._temra,self._recom,self._keys,self._keywo,mmcDefauV.keywo('recset'),chat_id)
                            if self._recom[1] !="" :
                                self.sending(tasRg)
                                self.sending(msgCreo.recom(self._recom[1],self._keywo))
                            else:
                                self.sending(tasRg)
                        else:
                            self.sending(tasRg)

                    elif "/rg_" in sette:
                        self._temra.update({ mmcDefauV.keywo('sf')[sette[4:6]] : sette[7:len(sette)] })
                        if self._sumo == 'outo':
                            tasRg=msgOuto.main(self._temra)
                        elif self._sumo == 'inco':
                            tasRg=msgInco.main(self._temra)
                        elif self._sumo == 'tran':
                            tasRg=msgTran.main(self._temra)
                        elif self._mod[-1] == 'edit':
                            tasRg=msgEdit.main(self._temra,self._list.get('uuid',''))

                        if self._keys in mmcDefauV.keywo('recset'):
                            self._recom = mmcdb.recomtxt(self._temra,self._recom,self._keys,self._keywo,mmcDefauV.keywo('recset'),chat_id)
                            if self._recom[1] !="" :
                                self.sending(tasRg)
                                self.sending(msgCreo.recom(self._recom[1],self._keywo))
                            else:
                                self.sending(tasRg+mainShort.woood(lingua,'rekeswd'))
                        else:
                            self.sending(tasRg+mainShort.woood(lingua,'rekeswd'))

            elif "/change" in text:
                if "/change_to_" in text:
                    if '/change_to_Income' in text:
                        self._temra['fromm'] = self._setting['genis']
                        self._temra['toooo'] = self._setting['dinco']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['incom']
                        self._temra['karen'] = self._setting['karen']
                        self._temra['tkare'] = self._setting['karen']
                        self._temra.update( { 'tpric' : self._temra.get('price','') } )
                        self.sending(msgInco.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                        # self._mod=mmctool.popmod(self._mod)
                        # self._mod=mmctool.apmod(self._mod,"inco")
                        self._sumo = 'inco'

                    elif '/change_to_Transfer' in text:
                        self._temra['fromm'] = self._setting['dinco']
                        self._temra['toooo'] = self._setting['dexpe']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['tanfe']
                        self._temra['karen'] = self._setting['karen']
                        self._temra['tkare'] = self._setting['karen']
                        self._temra.update( { 'tpric' : self._temra.get('price','') } )
                        self.sending(msgTran.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                        # self._mod=mmctool.popmod(self._mod)
                        # self._mod=mmctool.apmod(self._mod,"tran")
                        self._sumo = 'tran'

                    elif '/change_to_Expense' in text:
                        self._temra['fromm'] = self._setting['dexpe']
                        self._temra['toooo'] = self._setting['ovede']
                        self._temra['klass'] = ''
                        self._temra['karen'] = self._setting['karen']
                        self._temra['tkare'] = self._setting['karen']
                        self.sending(msgOuto.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                        # self._mod=mmctool.popmod(self._mod)
                        # self._mod=mmctool.apmod(self._mod,"outo")
                        self._sumo = 'outo'

                else:
                    self._recom = {}
                    if "/change_Currency_To" in text:
                        keywo = 'tk'
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sending(msgMain.selection(self._recom[1],'Currency (To)'))
                    elif "/change_Currency" in text:
                        keywo = 'kr'
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sending(msgMain.selection(self._recom[1],'Currency'))
                    elif "/change_Acc_From" in text:
                        keywo = 'fr'
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sending(msgMain.selection(self._recom[1],'Account (From)'))
                    elif "/change_Acc_To" in text:
                        keywo = 'to'
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sending(msgMain.selection(self._recom[1],'Account (To)'))
                    elif text.replace('/change_','') in ['Seller','Agent']:
                        keywo = 'sh'
                        self._recom = mmcdb.listSeller(self._temra.get('klass',''),'rg','rgs',keywo,chat_id)
                        if self._recom[1] != '':
                            self.sending(msgMain.selection(self._recom[1],text.replace('/change_','')))
                        else:
                            self.sending(mainShort.woood(lingua,'emptylist')+mainShort.woood(lingua,'rekeswd'))

            elif "/whats_now" in text:
                if self._sumo == 'outo':
                    self.sending(msgOuto.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._sumo == 'inco':
                    self.sending(msgInco.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._sumo == 'tran':
                    self.sending(msgTran.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._mod[-1] == 'edit':
                    self.sending(msgEdit.main(self._temra,self._list.get('uuid',''))+mainShort.woood(lingua,'rekeswd'))

            elif "/Back" in text:
                if self._sumo == 'outo':
                    self.sending(msgOuto.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._sumo == 'inco':
                    self.sending(msgInco.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._sumo == 'tran':
                    self.sending(msgTran.main(self._temra)+mainShort.woood(lingua,'rekeswd'))
                elif self._mod[-1] == 'edit':
                    self.sending(msgEdit.main(self._temra,self._list.get('uuid',''))+mainShort.woood(lingua,'rekeswd'))

        elif self._mod[-1] == 'defSett':
            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                mmctool.printbug("Discard Account Setting\n mod",self._mod,chat_id)
                self.sending(msgDefSet.discard())

                self._mod=mmctool.popmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

            elif "/Save" in text:
                mmcdb.changeSetting(self._setting,chat_id)
                self.sending(msgDefSet.fins(self._setting))
                self._mod=mmctool.popmod(self._mod)

            elif "/Explain" in text:
                self.sending(msgDefSet.warn())

            elif "/Back" in text:
                self.sending(msgDefSet.lista(self._setting))

            elif "/whats_now" in text:
                self.sending(msgDefSet.lista(self._temra))

            elif "/change_" in text:
                keywo = text[8:10]
                sfdic = mmcDefauV.keywo('sf')
                self._defSett = {}
                if '/change_lingua' in text:
                    keywo = 'lingua'
                    self._defSett = mmcdb.listLigua('ch',keywo,chat_id)
                    sasak = mmcDefauV.keywo('transle')['lingua']
                elif keywo in mmcDefauV.keywo('klass')['Acc']:
                    self._defSett = mmcdb.listAcc('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('transle')[kenwo]
                elif keywo in mmcDefauV.keywo('klass')['Kas']:
                    self._defSett = mmcdb.listKas('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('transle')[kenwo]
                elif keywo in mmcDefauV.keywo('klass')['Ken']:
                    self._defSett = mmcdb.listKen('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('transle')[kenwo]
                self.sending(msgMain.selection(self._defSett[1],sasak))

            elif "/ch" in text:
                if '/ch_lingua_' in text:
                    self._setting['lingua'] = text.replace('/ch_lingua_','')
                    tasDeSetCha=''
                else:
                    for sette in text.split(" "):
                        if "/chu_" in sette:
                            try:
                                self._setting.update({ mmcDefauV.keywo('sf')[sette[5:7]] : self._defSett[2][sette[8:len(sette)]] })
                                tasDeSetCha=''
                            except KeyError:
                                tasDeSetCha=msgMain.keywo('rgsWarn')
                        elif "/ch_" in sette:
                            self._setting[mmcDefauV.keywo('sf')[sette[4:6]]] = sette[7:len(sette)]
                            tasDeSetCha=''
                tasDeSetCha=tasDeSetCha+msgDefSet.lista(self._setting)
                self.sending(tasDeSetCha)

    def open(self, initial_msg, seed): # Welcome Region
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.printbug("Intitial",chat_id)
        mmctool.printbug("inti_msg",initial_msg,chat_id)
        self._mod = ['']
        self._setting = mmcdb.upgradeSetting(self._setting,chat_id)
        self._karatio = mmcdb.openKaratio()
        self._rawdb = mmcdb.opendb(chat_id)['raw']
        self._keydb = mmcdb.opendb(chat_id)['key']
        self._vez=0
        open(tool.path('log/mmcbot',usrid=auth.id())+tool.date(modde=1)+'.c','a').write('\n')

        if content_type != 'text':
            self.sending(msgMain.error(), modda = 1)
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._keywo = initial_msg["text"].replace(" ","_")
            self.sending(msgMain.home(self._keywo))

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.printbug("Received",chat_id)
        mmctool.printbug("msg",msg,chat_id)
        lingua = self._setting['lingua']

        if content_type != 'text':
            self.sending(msgMain.error(), modda = 1)
            self.close()
            return

        if msg["text"][0] == '/':
            self.comme(msg)
        else:
            self._keywo = msg["text"].replace("/","")

            if self._mod[-1] == '':
                self.sending(msgMain.home(self._keywo))

            elif self._mod[-1] == "list":
                if self._sumo == 'sachi':
                    self.sending(msgSachi.listKeywo(lingua,self._keywo))
                else:
                    self.sending(mainShort.woood(lingua,'emptysachi'))

            elif self._mod[-1] == "edit":
                tasEdit = msgEdit.keyword(self._keywo)
                self.sending(tasEdit)

            elif self._mod[-1] == 'statics':
                if self._statics['mode'] == 'abratio':
                    self.sending(msgAnali.abratioKeywo(lingua,self._keywo))
                elif self._statics['mode'] == 'atren':
                    self.sending(msgAnali.atrenKeywo(lingua,self._keywo))
                elif self._statics['mode'] == 'akaun':
                    self.sending(msgAnali.akaunKeywo(lingua,self._keywo))

            elif self._mod[-1] == "creo":
                if self._sumo == 'outo':
                    tasOut= msgCreo.keyword(self._keywo)
                    self.sending(tasOut)
                elif self._sumo == 'inco':
                    tasInco = msgInco.keyword(self._keywo)
                    self.sending(tasInco)
                elif self._sumo == 'tran':
                    tasTran = msgTran.keyword(self._keywo)
                    self.sending(tasTran)

            elif self._mod[-1] == 'defSett':
                numme = str(random.choice(range(10,100)))
                self._defSett={}
                try:
                    self._keywo.encode('latin-1')
                    self._defSett={1:["/ch_","_"+self._keywo],2:[]}
                except UnicodeEncodeError:
                    self._defSett={1:["/chu_","_"+numme+" "+self._keywo],2:{numme:self._keywo}}
                self.sending(msgDefSet.setup(self._keywo,self._defSett))

    def on__idle(self, event): # Timeout Region
        lingua = self._setting['lingua']
        self.sending(msgMain.timesout()+mainShort.woood(lingua,'cof') , modda = 1 )
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
