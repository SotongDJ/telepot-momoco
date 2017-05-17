import sys, os, traceback, telepot, time, json, random, pprint
import tool, auth, log, mmctool, mmcdb, mmcDefauV, mmcAnali
from libmsgMmc import msgMain, msgOuto, msgInco, msgTran, msgDefSet, msgList, msgEdit, msgAnali
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
        self._mod = []
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
        filla = open(tool.path('log/mmcbot',auth.id())+tool.date(5,'-'),'a')
        print("---"+text+"---")
        filla.write("""
--- pri: """+text+"""---
Time: """+tool.date(2,'-:')+"""
User: """+str(auth.id())+"""
keywo: """+pprint.pformat(self._keywo)+"""
keys: """+pprint.pformat(self._keys)+"""
mod: """+pprint.pformat(self._mod)+"""
temra: """+pprint.pformat(self._temra)+"""
recom: """+pprint.pformat(self._recom)+"""
defSett: """+pprint.pformat(self._defSett)+"""
setting: """+pprint.pformat(self._setting)+"""
--- pri fin ---
""")
        filla.close()

    def comme(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        text=msg['text']
        lingua = self._setting['ligua']
        if "/start" in text:
            if len(self._mod) == 0:
                tasStart=msgMain.start()+msgMain.short('cof')
            else:
                tasStart=msgMain.start()

            self.sender.sendMessage(tasStart)
            self._vez=mmctool.printvez(self._vez)

            if len(self._mod) == 0:
                self.close()

        elif "/help" in text:
            if len(self._mod) == 0:
                tasHelp=msgMain.help()+msgMain.short('cof')
            else:
                tasHelp=msgMain.help()

            self.sender.sendMessage(tasHelp)
            self._vez=mmctool.printvez(self._vez)

            if len(self._mod) == 0:
                self.close()

        elif "/setting" in text:
            self.sender.sendMessage(msgDefSet.main(self._setting))
            self._vez=mmctool.printvez(self._vez)

        elif "/modify_Setting" in text:
            self.sender.sendMessage(msgMain.short('refeson'))
            self._vez=mmctool.printvez(self._vez)
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            if len(self._mod) == 0:
                self._mod=mmctool.apmod(self._mod,'defSett')
            else:
                if self._mod[-1] != 'defSett':
                    self._mod=mmctool.apmod(self._mod,'defSett')

            tasDeSet=msgMain.short('refesfin')+msgDefSet.lista(self._setting)
            self.sender.sendMessage(tasDeSet)
            self._vez=mmctool.printvez(self._vez)

            if self._setting['defSettWarn'] == 0:
                self.sender.sendMessage(msgDefSet.warn())
                self._vez=mmctool.printvez(self._vez)
                self._setting['defSettWarn'] = 1
                mmcdb.changeSetting(self._setting,chat_id)

        elif "/exit" in text:
            self.sender.sendMessage(msgMain.short('bye'))
            self._vez=mmctool.printvez(self._vez)
            self.close()

        elif "/new" in text:
            self.sender.sendMessage(msgMain.short('refeson'))
            self._vez=mmctool.printvez(self._vez)
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            if len(self._mod) == 0:
                self._temra["datte"] = tool.date(1,'-')
                self._temra['fromm'] = self._setting['dexpe']
                self._temra['toooo'] = self._setting['ovede']
                self._temra['karen'] = self._setting['karen']
                self._temra['tkare'] = self._setting['karen']
            if self._keywo != "":
                if '/' not in self._keywo:
                    tasOut= msgMain.short('refesfin')+msgOuto.main(self._temra)
                    tasOut= tasOut + msgMain.short('band') + msgOuto.keyword(self._keywo)
                    self.sender.sendMessage(tasOut)
                    self._vez=mmctool.printvez(self._vez)
            else:
                tasOut=msgMain.short('refesfin')+msgOuto.main(self._temra)+msgMain.short('rekeswd')
                self.sender.sendMessage(tasOut)
                self._vez=mmctool.printvez(self._vez)
            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod(self._mod,"outo")

        elif "/list" in text:
            self.sender.sendMessage(msgMain.short('refeson'))
            self._vez=mmctool.printvez(self._vez)
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            if len(self._mod) == 0:
                lastdate = list(self._keydb['datte'])
                lastdate.sort()
                try:
                    self._list.update({ 'datte' : lastdate[-1] })
                except IndexError :
                    self._list.update({ 'datte' : '' })
            tasList=msgMain.short('refesfin')+msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id))
            self.sender.sendMessage(tasList)
            self._vez=mmctool.printvez(self._vez)
            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod(self._mod,"list")

        elif "/Edit" in text:
            if self._mod[-1] == "list":
                uuid = self._list.get('uuid','')
                if uuid !='':
                    self._mod = mmctool.apmod(self._mod,'edit')
                    self._keywo = ''
                    self._temra.update(self._rawdb.get(uuid,''))
                    self.sender.sendMessage(msgEdit.main(self._temra,uuid)+msgMain.short('rekeswd'))
                    self._vez = mmctool.printvez(self._vez)
                else:
                    self.sender.sendMessage(msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                    self._vez = mmctool.printvez(self._vez)
            else:
                self.sender.sendMessage(msgMain.keywo('whatsnow'))
                self._vez = mmctool.printvez(self._vez)

        elif "/statics" in text:
            self.sender.sendMessage(msgMain.short('refeson'))
            self._vez=mmctool.printvez(self._vez)
            mmcdb.refesdb(chat_id)
            self._rawdb = mmcdb.opendb(chat_id)['raw']
            self._keydb = mmcdb.opendb(chat_id)['key']
            mmcdb.refesKaratio(self._keydb)
            self._karatio = mmcdb.openKaratio()
            tasList=msgMain.short('refesfin')+msgAnali.chooseMode(lingua)
            self.sender.sendMessage(tasList)
            self._vez=mmctool.printvez(self._vez)
            self._mod=mmctool.popmod(self._mod)
            self._mod=mmctool.apmod(self._mod,"statics")

        elif len(self._mod) == 0:
            self.sender.sendMessage(msgMain.bored()+msgMain.short('cof'))
            self._vez=mmctool.printvez(self._vez)
            self.close()

        elif self._mod[-1] == "list":
            if "/whats_now" in text:
                self.sender.sendMessage(msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                self._vez=mmctool.printvez(self._vez)

            elif "/Back" in text:
                self._list.update({'uuid' : '' })
                self.sender.sendMessage(msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                self._vez=mmctool.printvez(self._vez)

            elif "/Close" in text:
                self.sender.sendMessage(msgList.disca()+msgMain.short('cof'))
                self._vez=mmctool.printvez(self._vez)
                self._mod=[]
                self.close()

            elif "/uuid_" in text:
                print('uuid')
                for sette in text.split(' '):
                    if "/uuid_" in sette:
                        self._list.update({'uuid' : sette.replace('/uuid_','') })
                        self.sender.sendMessage(msgList.single(self._list.get('uuid',''),chat_id,self._rawdb))
                        self._vez=mmctool.printvez(self._vez)

            elif "/Choose_" in text:
                for sette in text.split(' '):
                    if "/Choose_" in sette:
                        keywo = sette.replace("/Choose_",'').replace('_','-')
                setta = mmctool.filteDate(list(self._keydb['datte']),keywo)
                testa = mmctool.cmdzDate(setta)
                self.sender.sendMessage(msgList.change(keywo,testa))
                self._vez=mmctool.printvez(self._vez)

            elif "/ch_" in text:
                tasta = ''
                for takso in text.split(' '):
                    if '/ch_' in takso:
                        tasta = takso.replace('/ch_','').replace('_','-')
                self._list.update({'datte' : tasta })
                self.sender.sendMessage(msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                self._vez=mmctool.printvez(self._vez)

        elif self._mod[-1] == "statics":
            if "/Analysis" in text:
                if self._statics['mode'] != '':
                    if self._statics['mode'] == 'atren':
                        self._statics['targe'] = '－－'
                    print('statics : '+pprint.pformat(self._statics, compact=True))
                    if '' in self._statics.values():
                        self.sender.sendMessage(msgMain.short('analiWarn'))
                    else:
                        if self._statics['mode'] == 'abratio':
                            medio = mmcAnali.abratio(chat_id,self._statics)
                            secto = msgAnali.abratioResut(lingua,medio)
                        elif self._statics['mode'] == 'atren':
                            medio = mmcAnali.atren(chat_id,self._statics)
                            secto = msgAnali.atrenResut(lingua,medio)
                        for lun in secto:
                            self.sender.sendMessage(lun)
                            self._vez=mmctool.printvez(self._vez)
                else:
                    self.sender.sendMessage(msgMain.keywo('whatsnow'))

            elif "/whats_now" in text:
                self.sender.sendMessage(msgMain.keywo('whatsnow'))
                self._vez = mmctool.printvez(self._vez)

            elif "/Back" in text:
                if self._statics['mode'] != '':
                    if self._statics['mode'] == 'abratio':
                        self.sender.sendMessage(msgAnali.chooseMode(lingua))
                        self._vez=mmctool.printvez(self._vez)
                        self._statics['mode'] = ''
                    elif self._statics['mode'] == 'atren':
                        self.sender.sendMessage(msgAnali.chooseMode(lingua))
                        self._vez=mmctool.printvez(self._vez)
                        self._statics['mode'] = ''
                else:
                    self._statics = mmcDefauV.keywo('statics')
                    self.sender.sendMessage(msgAnali.chooseMode(lingua))
                    self._vez=mmctool.printvez(self._vez)

            elif "/Close" in text:
                self.sender.sendMessage(msgAnali.disca(lingua)+msgMain.short('cof'))
                self._vez=mmctool.printvez(self._vez)
                self._mod=[]
                self.close()

            elif '/set_Mode_as_' in text:
                if '/set_Mode_as_abratio' in text:
                    self._statics['mode'] = 'abratio'
                    self.sender.sendMessage(msgAnali.abratioMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)
                elif '/set_Mode_as_atren' in text:
                    self._statics['mode'] = 'atren'
                    self.sender.sendMessage(msgAnali.atrenMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)

            elif '/change_' in text:
                skdic = mmcDefauV.keywo('ssalk')
                if '/change_conda' in text:
                    keywo = 'conda'
                elif '/change_targe' in text:
                    keywo = 'targe'
                titil = skdic.get(keywo,'')
                self.sender.sendMessage(msgMain.selection(mmcAnali.listClass(keywo),titil))
                self._vez=mmctool.printvez(self._vez)

            elif '/set_conda_as_' in text:
                self._statics.update({ 'conda' : text.replace('/set_conda_as_','') })
                if self._statics['mode'] == 'abratio':
                    self.sender.sendMessage(msgAnali.abratioMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)
                elif self._statics['mode'] == 'atren':
                    self.sender.sendMessage(msgAnali.atrenMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)

            elif '/set_targe_as_' in text:
                self._statics.update({ 'targe' : text.replace('/set_targe_as_','') })
                if self._statics['mode'] == 'abratio':
                    self.sender.sendMessage(msgAnali.abratioMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)
                elif self._statics['mode'] == 'atren':
                    self.sender.sendMessage(msgAnali.atrenMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)

            elif '/set_Leve_in_' in text:
                if '/set_Leve_in_Day' in text:
                    self._statics.update({ 'leve' : 10 })
                elif '/set_Leve_in_Month' in text:
                    self._statics.update({ 'leve' : 7 })
                elif '/set_Leve_in_Year' in text:
                    self._statics.update({ 'leve' : 4 })

                if self._statics['mode'] == 'abratio':
                    self.sender.sendMessage(msgAnali.abratioMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)
                elif self._statics['mode'] == 'atren':
                    self.sender.sendMessage(msgAnali.atrenMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)

            elif '/set_as_' in text:
                if '/set_as_dtempo' in text:
                    self._statics.update({ 'dtempo' : self._keywo })
                elif '/set_as_utempo' in text:
                    self._statics.update({ 'utempo' : self._keywo })
                elif '/set_as_conde' in text:
                    self._statics.update({ 'conde' : self._keywo })
                elif '/set_as_targe' in text:
                    self._statics.update({ 'targe' : self._keywo })

                if self._statics['mode'] == 'abratio':
                    self.sender.sendMessage(msgAnali.abratioMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)
                elif self._statics['mode'] == 'atren':
                    self.sender.sendMessage(msgAnali.atrenMain(lingua,self._statics))
                    self._vez=mmctool.printvez(self._vez)

        elif self._mod[-1] in ['outo','inco','tran','edit']:
            if "/Discard" in text:
                self._keywo = ''
                for key in self._temra.keys():
                    self._temra.update({ key : '' })

                if self._mod[-1] == 'edit':
                    mmctool.printbug("Discard editing\n mod",self._mod,chat_id)
                    self.sender.sendMessage(msgEdit.discar()+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)
                else:
                    mmctool.printbug("Discard record\n mod",self._mod,chat_id)
                    self.sender.sendMessage(msgOuto.discard()+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)

                self._mod=mmctool.popmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

                if self._mod[-1] != 'edit':
                    self.close()

            elif "/Save" in text:
                if self._mod[-1] == 'edit':
                    uuid = self._list.get('uuid','')
                    record = mmcdb.chRaw(self._temra,uuid,chat_id)
                else:
                    record = mmcdb.addRaw(chat_id,self._temra)

                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(msgOuto.finis(self._temra)+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(msgInco.finis(self._temra)+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(msgTran.finis(self._temra)+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'edit':
                    self.sender.sendMessage(msgEdit.fin(uuid,chat_id,record)+msgMain.short('cof'))
                    self._vez=mmctool.printvez(self._vez)

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
                elif "/set_as_Place" in text:
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
                    self._temra.update({ 'price' : self._keywo })
                    self._keys='price'
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
                if self._mod[-1] == 'outo':
                    tasRef=msgOuto.main(self._temra)
                elif self._mod[-1] == 'inco':
                    tasRef=msgInco.main(self._temra)
                elif self._mod[-1] == 'tran':
                    tasRef=msgTran.main(self._temra)
                elif self._mod[-1] == 'edit':
                    tasRef=msgEdit.main(self._temra,self._list.get('uuid',''))

                if self._keys in ['namma', 'klass', 'shoop', 'price']:
                    self._recom = mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],chat_id)
                    if self._recom[1] !="" :
                        self.sender.sendMessage(tasRef)
                        self._vez=mmctool.printvez(self._vez)
                        self.sender.sendMessage(msgOuto.recom(self._recom[1],self._keywo))
                        self._vez=mmctool.printvez(self._vez)
                    else:
                        self.sender.sendMessage(tasRef+msgMain.short('rekeswd'))
                        self._vez=mmctool.printvez(self._vez)
                else:
                    self.sender.sendMessage(tasRef+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)

            elif "/rg" in text :
                for sette in text.split(" "):
                    if "/rgs_" in sette:
                        try:
                            self._temra.update({ mmcDefauV.keywo('sf')[sette[5:7]] : self._recom[2][sette[8:len(sette)]] })
                            if self._mod[-1] == 'outo':
                                tasRgs=msgOuto.main(self._temra)
                            elif self._mod[-1] == 'inco':
                                tasRgs=msgInco.main(self._temra)
                            elif self._mod[-1] == 'tran':
                                tasRgs=msgTran.main(self._temra)
                            elif self._mod[-1] == 'edit':
                                tasRgs=msgEdit.main(self._temra,self._list.get('uuid',''))
                            tasRgs = tasRgs +'\n\n'+msgOuto.recom(self._recom[1],self._keywo)
                            self.sender.sendMessage(tasRgs)
                            self._vez=mmctool.printvez(self._vez)
                            #self.sender.sendMessage(msgOuto.recom(self._recom[1],self._keywo))
                            self._vez=mmctool.printvez(self._vez)
                        except KeyError:
                            print("KeyError : Doesn't Exist or Expired")

                            if self._mod[-1] == 'outo':
                                tasRgs=msgMain.short('rgsWarn')+msgOuto.main(self._temra)+msgMain.short('rekeswd')
                            elif self._mod[-1] == 'inco':
                                tasRgs=msgMain.short('rgsWarn')+msgInco.main(self._temra)+msgMain.short('rekeswd')
                            elif self._mod[-1] == 'tran':
                                tasRgs=msgMain.short('rgsWarn')+msgTran.main(self._temra)+msgMain.short('rekeswd')
                            elif self._mod[-1] == 'edit':
                                tasRgs=msgMain.short('rgsWarn')+msgEdit.main(self._temra,self._list.get('uuid',''))+msgMain.short('rekeswd')

                            self.sender.sendMessage(tasRgs)
                            self._vez=mmctool.printvez(self._vez)

                    elif "/rg_" in sette:
                        self._temra.update({ mmcDefauV.keywo('sf')[sette[4:6]] : sette[7:len(sette)] })
                        if self._mod[-1] == 'outo':
                            tasRg=msgOuto.main(self._temra)
                        elif self._mod[-1] == 'inco':
                            tasRg=msgInco.main(self._temra)
                        elif self._mod[-1] == 'tran':
                            tasRg=msgTran.main(self._temra)
                        elif self._mod[-1] == 'edit':
                            tasRg=msgEdit.main(self._temra,self._list.get('uuid',''))
                        self.sender.sendMessage(tasRg)
                        self._vez=mmctool.printvez(self._vez)
                        self.sender.sendMessage(msgOuto.recom(self._recom[1],self._keywo))
                        self._vez=mmctool.printvez(self._vez)

            elif "/change" in text:
                if "/change_to_" in text:
                    if '/change_to_Income' in text:
                        self._temra['fromm'] = self._setting['genis']
                        self._temra['toooo'] = self._setting['dinco']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['incom']
                        self.sender.sendMessage(msgInco.main(self._temra)+msgMain.short('rekeswd'))
                        self._vez=mmctool.printvez(self._vez)
                        self._mod=mmctool.popmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"inco")

                    elif '/change_to_Transfer' in text:
                        self._temra['fromm'] = self._setting['dinco']
                        self._temra['toooo'] = self._setting['dexpe']
                        self._temra['shoop'] = ''
                        self._temra['klass'] = self._setting['tanfe']
                        self.sender.sendMessage(msgTran.main(self._temra)+msgMain.short('rekeswd'))
                        self._vez=mmctool.printvez(self._vez)
                        self._mod=mmctool.popmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"tran")

                    elif '/change_to_Expense' in text:
                        self._temra['fromm'] = self._setting['dexpe']
                        self._temra['toooo'] = self._setting['ovede']
                        self._temra['klass'] = self._setting['']
                        self.sender.sendMessage(msgOuto.main(self._temra)+msgMain.short('rekeswd'))
                        self._vez=mmctool.printvez(self._vez)
                        self._mod=mmctool.popmod(self._mod)
                        self._mod=mmctool.apmod(self._mod,"outo")

                else:
                    self._recom = {}
                    if "/change_Currency_To" in text:
                        keywo = 'tk'
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(msgMain.selection(self._recom[1],'Currency (To)'))
                        self._vez=mmctool.printvez(self._vez)
                    elif "/change_Currency" in text:
                        keywo = 'kr'
                        self._recom = mmcdb.listKen('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(msgMain.selection(self._recom[1],'Currency'))
                        self._vez=mmctool.printvez(self._vez)
                    elif "/change_Acc_From" in text:
                        keywo = 'fr'
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(msgMain.selection(self._recom[1],'Account (From)'))
                        self._vez=mmctool.printvez(self._vez)
                    elif "/change_Acc_To" in text:
                        keywo = 'to'
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(msgMain.selection(self._recom[1],'Account (To)'))
                        self._vez=mmctool.printvez(self._vez)
                    elif text.replace('/change_','') in ['Seller','Agent','Place']:
                        keywo = 'sh'
                        self._recom = mmcdb.listAcc('rg','rgs',keywo,chat_id)
                        self.sender.sendMessage(msgMain.selection(self._recom[1],text.replace('/change_','')))
                        self._vez=mmctool.printvez(self._vez)

            elif "/whats_now" in text:
                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(msgOuto.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(msgInco.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(msgTran.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'edit':
                    self.sender.sendMessage(msgEdit.main(self._temra,self._list.get('uuid',''))+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)

            elif "/Back" in text:
                if self._mod[-1] == 'outo':
                    self.sender.sendMessage(msgOuto.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'inco':
                    self.sender.sendMessage(msgInco.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'tran':
                    self.sender.sendMessage(msgTran.main(self._temra)+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)
                elif self._mod[-1] == 'edit':
                    self.sender.sendMessage(msgEdit.main(self._temra,self._list.get('uuid',''))+msgMain.short('rekeswd'))
                    self._vez=mmctool.printvez(self._vez)

        elif self._mod[-1] == 'defSett':
            if "/Discard" in text:
                self._keywo = ""
                for key in self._temra.keys():
                    self._temra[key]=""

                mmctool.printbug("Discard Account Setting\n mod",self._mod,chat_id)
                self.sender.sendMessage(msgDefSet.discard())
                self._vez=mmctool.printvez(self._vez)

                self._mod=mmctool.popmod(self._mod)
                mmctool.printbug("Changed back mode\n mod",self._mod,chat_id)

            elif "/Save" in text:
                mmcdb.changeSetting(self._setting,chat_id)
                self.sender.sendMessage(msgDefSet.fins(self._setting))
                self._vez=mmctool.printvez(self._vez)
                self._mod=mmctool.popmod(self._mod)

            elif "/Explain" in text:
                self.sender.sendMessage(msgDefSet.warn())
                self._vez=mmctool.printvez(self._vez)

            elif "/Back" in text:
                self.sender.sendMessage(msgDefSet.lista(self._setting))
                self._vez=mmctool.printvez(self._vez)

            elif "/whats_now" in text:
                self.sender.sendMessage(msgDefSet.lista(self._temra))
                self._vez=mmctool.printvez(self._vez)

            elif "/change_" in text:
                keywo = text[8:10]
                sfdic = mmcDefauV.keywo('sf')
                self._defSett = {}
                if '/change_ligua' in text:
                    keywo = 'ligua'
                    self._defSett = mmcdb.listLigua('ch',keywo,chat_id)
                    sasak = 'Language'
                elif keywo in mmcDefauV.keywo('klass')['Acc']:
                    self._defSett = mmcdb.listAcc('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('ssalk')[kenwo]
                elif keywo in mmcDefauV.keywo('klass')['Kas']:
                    self._defSett = mmcdb.listKas('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('ssalk')[kenwo]
                elif keywo in mmcDefauV.keywo('klass')['Ken']:
                    self._defSett = mmcdb.listKen('ch','chu',keywo,chat_id)
                    kenwo = sfdic[keywo]
                    sasak = mmcDefauV.keywo('ssalk')[kenwo]
                self.sender.sendMessage(msgMain.selection(self._defSett[1],sasak))
                self._vez=mmctool.printvez(self._vez)

            elif "/ch" in text:
                if '/ch_ligua_' in text:
                    self._setting['ligua'] = text.replace('/ch_ligua_','')
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
                self.sender.sendMessage(tasDeSetCha)
                self._vez=mmctool.printvez(self._vez)

    def open(self, initial_msg, seed): # Welcome Region
        content_type, chat_type, chat_id = telepot.glance(initial_msg)
        self.printbug("Intitial",chat_id)
        mmctool.printbug("inti_msg",initial_msg,chat_id)
        self._mod = []
        self._setting = mmcdb.upgradeSetting(self._setting,chat_id)
        self._karatio = mmcdb.openKaratio()
        self._rawdb = mmcdb.opendb(chat_id)['raw']
        self._keydb = mmcdb.opendb(chat_id)['key']
        self._vez=0
        open(tool.path('log/mmcbot',auth.id())+tool.date(1,'-')+'.c','a').write('\n')
        self._vez=mmctool.printvez(self._vez)

        if content_type != 'text':
            self.sender.sendMessage(msgMain.error())
            self._vez=mmctool.printvez(self._vez)
            self.close()
            return

        if "/" in initial_msg["text"]:
            self.comme(initial_msg)
        else:
            if "/" not in initial_msg["text"]:
                self._keywo = initial_msg["text"].replace(" ","_")
            self.sender.sendMessage(msgMain.home(self._keywo))
            self._vez=mmctool.printvez(self._vez)

        return True  # prevent on_message() from being called on the initial message

    def on_chat_message(self, msg): # Each Msg
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.printbug("Received",chat_id)
        mmctool.printbug("msg",msg,chat_id)
        lingua = self._setting['ligua']

        if content_type != 'text':
            self.sender.sendMessage(msgMain.error())
            self.close()
            return

        if msg["text"][0] == '/':
            self.comme(msg)
        else:
            self._keywo = msg["text"].replace("/","")

            if len(self._mod) == 0:
                self.sender.sendMessage(msgMain.home(self._keywo))
                self._vez=mmctool.printvez(self._vez)

            elif self._mod[-1] == "list":
                self.sender.sendMessage(msgList.main(self._list.get('datte',''),mmcdb.listList(self._list.get('datte',''),chat_id)))
                self._vez=mmctool.printvez(self._vez)
            elif self._mod[-1] == "edit":
                tasEdit = msgEdit.main(self._temra,self._list.get('uuid',''))
                tasEdit = tasEdit + msgMain.short('band')
                tasEdit = tasEdit + msgEdit.keyword(self._keywo)
                self.sender.sendMessage(tasEdit)
                self._vez=mmctool.printvez(self._vez)

            elif self._mod[-1] == 'statics':
                if self._statics['mode'] == 'abratio':
                    self.sender.sendMessage(msgAnali.abratioKeywo(lingua,self._keywo))
                    self._vez=mmctool.printvez(self._vez)
                elif self._statics['mode'] == 'atren':
                    self.sender.sendMessage(msgAnali.atrenKeywo(lingua,self._keywo))
                    self._vez=mmctool.printvez(self._vez)

            elif self._mod[-1] == "outo":
                tasOut= msgOuto.main(self._temra)
                tasOut= tasOut + msgMain.short('band') + msgOuto.keyword(self._keywo)
                self.sender.sendMessage(tasOut)
                self._vez=mmctool.printvez(self._vez)
            elif self._mod[-1] == "inco":
                tasInco = msgInco.main(self._temra)
                tasInco = tasInco + msgMain.short('band') + msgInco.keyword(self._keywo)
                self.sender.sendMessage(tasInco)
                self._vez=mmctool.printvez(self._vez)
            elif self._mod[-1] == "tran":
                tasTran = msgTran.main(self._temra)
                tasTran = tasTran + msgMain.short('band') + msgTran.keyword(self._keywo)
                self.sender.sendMessage(tasTran)
                self._vez=mmctool.printvez(self._vez)

            elif self._mod[-1] == 'defSett':
                numme = str(random.choice(range(10,100)))
                self._defSett={}
                try:
                    self._keywo.encode('latin-1')
                    self._defSett={1:["/ch_","_"+self._keywo],2:[]}
                except UnicodeEncodeError:
                    self._defSett={1:["/chu_","_"+numme+" "+self._keywo],2:{numme:self._keywo}}
                self.sender.sendMessage(msgDefSet.setup(self._keywo,self._defSett))
                self._vez=mmctool.printvez(self._vez)

    def on__idle(self, event): # Timeout Region
        self.sender.sendMessage(msgMain.timesout()+msgMain.short('cof'))
        self._vez=mmctool.printvez(self._vez)
        self.close()

key=json.load(open("database/key","r"))
TOKEN = key["momocobot"]

bot = telepot.DelegatorBot(TOKEN, [pave_event_space()(
    per_chat_id(), create_open, User, timeout=100),]
    )
bot.message_loop(run_forever='Listening ...')
