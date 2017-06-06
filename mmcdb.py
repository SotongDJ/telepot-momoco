import json, random, hashlib, pprint, requests
import tool, mmctool, mmcDefauV
# fille = __
# mmcdb.writedb(fille,'raw',mmcdb.opencsv(fille,','))

def opendb(usrid):
    try:
        faale = open(tool.path("momoco",usrid)+"record.json","r")
        record = json.load(faale)
        mmctool.printbug("Load Record",'',usrid)
        faale.close()
        return record
    except FileNotFoundError:
        mmctool.printbug('FileNotFoundError','',usrid)
        return {'raw':{},'key':{},'hash':{}}

def openSetting(usrid):
    try:
        faale = open(tool.path("momoco",usrid)+"setting.json","r")
        setting = json.load(faale)
        mmctool.printbug("Load Setting",'',usrid)
        faale.close()
        return setting
    except FileNotFoundError:
        mmctool.printbug('FileNotFoundError','',usrid)
        setting = mmcDefauV.keywo('setting')
        return setting

def openKaratio():
    tool.ckpath('database/opt/momoco/','karen.json')
    faale = open('database/opt/momoco/karen.json',"r")
    try:
        karatio = json.load(faale)
    except ValueError:
        karatio = {}
    faale.close()
    return karatio

def refesKaratio(keydb):
    karatio = openKaratio()
    curre = set(list(keydb.get('karen'))+list(keydb.get('tkare')))
    kara = []
    for m in curre:
        for n in curre:
            if m != n:
                kara.append(m+n)
    setta = '\"'+'\",\"'.join(kara)+'\"'
    urlla = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20('+setta+')&format=json&env=store://datatables.org/alltableswithkeys'
    datta = json.loads(requests.get(urlla).text)
    for m in datta['query']['results']['rate']:
        karatio.update({ m['id'] : m['Rate'] })
    faale = open('database/opt/momoco/karen.json',"w")
    json.dump(karatio,faale)
    faale.close()

def resetKaratio(keydb):
    karatio = {}
    curre = set(list(keydb.get('karen'))+list(keydb.get('tkare')))
    kara = []
    for m in curre:
        for n in curre:
            if m != n:
                kara.append(m+n)
    setta = '\"'+'\",\"'.join(kara)+'\"'
    urlla = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20('+setta+')&format=json&env=store://datatables.org/alltableswithkeys'
    datta = json.loads(requests.get(urlla).text)
    for m in datta['query']['results']['rate']:
        karatio.update({ m['id'] : m['Rate'] })
    faale = open('database/opt/momoco/karen.json',"w")
    json.dump(karatio,faale)
    faale.close()

""" mmcdb.opencsv( ,',')"""
def opencsv(fille,keywo):
    result = {}
    numo = 0
    for linne in open(fille).read().splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        elif linne[0] != "#":
            zero = '9000'
            uri = tool.date(3,'')
            nama = uri+zero[0:4-len(str(numo))]+str(numo)
            result[nama]={}
            word = linne.split(keywo)
            for n in range(0,len(word)):
                result[nama][keys[n]]=word[n]
            numo = numo + 1
    return result

""" record = mmcdb.addRaw(chat_id,self._temra)"""
def addRaw(usrid,temra):
    record = opendb(usrid)
    timta = tool.date(3,'0000')
    record["raw"][timta] = temra
    mmctool.printbug("Add Record",'',usrid)
    faale = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(record,faale)
    faale.close()
    return record

""" record = mmcdb.addRaw(chat_id,self._temra)"""
def chRaw(temra,uuid,usrid):
    record = opendb(usrid)
    record["raw"].update( { uuid : temra } )
    mmctool.printbug("change Record",'',usrid)
    faale = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(record,faale)
    faale.close()
    return record

def diffdb(a,b):
    for m in a.keys():
        if a.get(m) != b.get(m):
            c=pprint.pformat(a.get(m)).replace('\n', '  ')
            d=pprint.pformat(b.get(m)).replace('\n', '  ')
            print(c+'\n'+d)

def genKey(rawdb):
    keydb = {}
    eledb = {}
    valudb = {}
    for uuid in rawdb.keys():
        for eleme in rawdb.get(uuid,{}):
            valuh = rawdb[uuid].get(eleme,'')
            if valuh != '':
                tadd = eledb.get(eleme,{})

                mobb = tadd.get(valuh,[])
                mobb.append(uuid)
                mobb = sorted(list(set(mobb)))

                tadd.update( { valuh : mobb } )
                eledb.update({ eleme : tadd })
    return eledb

""" genHash(rawdb)"""
def genHash(rawdb):
    hashdb = {}
    for uuid in list(rawdb.keys()):
        hasa = hashlib.sha512()
        if rawdb.get(uuid,{}) != {}:
            hasa.update((",".join(set(list(rawdb.get(uuid,{}).values())))).encode("utf-8"))
            hashdb.update( { uuid : hasa.hexdigest() } )
    return hashdb

def changeSetting(libra,usrid):
    faale = open(tool.path("momoco",usrid)+"setting.json",'w')
    json.dump(libra,faale)
    faale.close()

def ckrpt(h):
    l={}
    for n in h.keys():
        if '' in h[n].values():
            for m in h[n].keys():
                if m != 'desci':
                    if h[n][m] == '':
                        l.update( { n : m } )
    return l

def ckdb(a,b):
    l={}
    for m in a:
        for n in a[m]:
            if n != '':
                if sorted(a[m][n]) !=  sorted(b[m][n]):
                    l.update( { m+' '+n  : [sorted(b[m][n]) , sorted(a[m][n])] } )
    return l

""" fixAcc(libra[raw],usrid)"""
def fixAcc(rawdb,usrid):
    setti = openSetting(usrid)
    #rawdb = opendb(usrid).get('raw',{})

    tanfe = setti.get('tanfe','Transfer')
    incom = setti.get('incom','Income')

    dinco = setti.get('dinco','Bank')
    dexpe = setti.get('dexpe','Cash')
    genis = setti.get('genis','Income')
    ovede = setti.get('ovede','Expense')

    karen = setti.get('karen','')

    for n in list(rawdb):
        if rawdb[n].get('klass','') == incom:
            if rawdb[n].get('price','') == '':
                rawdb[n].update( {'price' : rawdb[n].get('tpric','') })
            if rawdb[n].get('karen','') == '':
                rawdb[n].update( {'karen' : rawdb[n].get('tkare','') })
            if rawdb[n].get('fromm','') == '':
                rawdb[n].update( {'fromm' : genis })
            if rawdb[n].get('toooo','') == '':
                rawdb[n].update( {'toooo' : dinco })
        elif rawdb[n].get('klass','') in tanfe:
            if rawdb[n].get('tpric','') == '':
                rawdb[n].update( {'tpric' : rawdb[n].get('price','') })
            if rawdb[n].get('tkare','') == '':
                rawdb[n].update( {'tkare' : rawdb[n].get('karen','') })
            if rawdb[n].get('fromm','') == '':
                rawdb[n].update( {'fromm' : dinco })
            if rawdb[n].get('toooo','') == '':
                rawdb[n].update( {'toooo' : dexpe })
        else:
            rawdb[n].update( {'tpric' : rawdb[n].get('price','') })
            rawdb[n].update( {'tkare' : rawdb[n].get('karen','') })
            if rawdb[n].get('fromm','') == '':
                rawdb[n].update( {'fromm' : dexpe })
            if rawdb[n].get('toooo','') == '':
                rawdb[n].update( {'toooo' : ovede })
    return rawdb

""" mmcdb.refesdb(chat_id)"""
def refesdb(usrid):
    libra = {}
    rawdb = opendb(usrid)['raw']
    rawdb = fixAcc(rawdb,usrid)
    libra.update( {'raw' : rawdb})
    keydb = genKey(rawdb)
    libra.update( {'key' : keydb})
    hashdb=genHash(rawdb)
    libra.update( {'hash' : hashdb})
    faale = open(tool.path("momoco",usrid)+"record.json",'w')
    json.dump(libra,faale)
    faale.close()

""" mmcdb.upgradeSetting(self._setting,chat_id)"""
def upgradeSetting(lib,usrid):
    libra = openSetting(usrid)
    if set(libra.keys()) == set(lib.keys()):
        return libra
    else:
        for keywo in libra.keys():
            lib[keywo]=libra[keywo]
        changeSetting(lib,usrid)
        return lib

""" importRaw(usrid,lib)"""
def importRaw(usrid,lib):
    refesdb(usrid)
    lib=fixAcc(lib,usrid)
    source = opendb(usrid)
    for uuid in list(lib.keys()):
        hasa = hashlib.sha512()
        if lib[uuid] != {}:
            hasa.update((",".join(set(list(lib[uuid].values())))).encode("utf-8"))
            if hasa.hexdigest() not in list(source['hash'].values()):
                source['raw'][uuid]=lib[uuid]
    filla = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(source,filla)
    filla.close()

def recoma(keys,usrid):
    refesdb(usrid)
    libra = opendb(usrid)
    listo = []
    try:
        for veluo in list(libra[keys].keys()):
            for uuid in libra[keys][veluo]:
                listo.append(veluo)
    except KeyError:
        mmctool.printbug("KeyError",'',usrid)
    lista = []
    setto = set(listo)
    for n in [1,2,3,4,5]:
        try:
            dan = max(setto,key=listo.count)
            lista.append(dan)
            setto.remove(dan)
        except ValueError:
            mmctool.printbug("No keywo",'',usrid)
    return lista

""" recomb(self._keys,self._keywo,deskey,usrid) """
def recomb(srckey,veluo,deskey,usrid):
    #refesdb(usrid)
    libre = opendb(usrid)
    listo = []
    try:
        for uuid in libre['key'][srckey][veluo]:
            listo.append(libre['raw'][uuid][deskey])
    except KeyError:
        mmctool.printbug("KeyError",'',usrid)
    lista = []
    setto = set(listo)
    for n in [1,2,3,4]:
        try:
            dan = max(setto,key=listo.count)
            lista.append(dan)
            setto.remove(dan)
        except ValueError:
            mmctool.printbug("No keywo",'',usrid)
    return lista

""" recomc(self._keys,self._keywo,knolib,unoset,usrid) """
def recomc(srckey,veluo,knolib,unoset,usrid):
    #refesdb(usrid)
    rawdb = opendb(usrid).get('raw',{})
    keydb = opendb(usrid).get('key',{})
    rslib = {}
    for uuid in keydb.get(srckey,{}).get(veluo,[]):
        mdlib = {}
        for rawkey in rawdb.get(uuid,{}):
            if rawkey in unoset:
                mdlib.update({ rawkey : rawdb.get(uuid,{}).get(rawkey,'') })
            elif rawkey in knolib.keys():
                if rawdb.get(uuid,{}).get(rawkey,'') != knolib.get(rawkey,''):
                    mdlib.update({ 'mismo' : 'no' })
        if mdlib.get('mismo','') != 'no':
            for mdkey in mdlib.keys():
                mdlist = rslib.get(mdkey,[])
                mdlist.append(mdlib.get(mdkey,''))
                rslib.update({ mdkey : [x for x in mdlist if x != ''] })
    for rskey in rslib:
        lista = []
        listo = rslib.get(rskey,[])
        setto = set(listo)
        for n in [1,2,3,4,5]:
            try:
                dan = max(setto,key=listo.count)
                lista.append(dan)
                setto.remove(dan)
            except ValueError:
                mmctool.printbug("Finish",'',usrid)
        rslib.update({ rskey : lista })
    return rslib

""" mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],chat_id) """
def recomtxt(temra,keysa,keywo,deset,usrid):
    #refesdb(usrid)
    fsdic = mmcDefauV.keywo('fs')
    skdic = mmcDefauV.keywo('ssalk')

    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0

    knolib = {}
    knoset = [ x for x in deset if temra.get(x,'') != '' ]
    unoset = set(deset) - set(knoset)

    for knokey in knoset:
        knolib.update({ knokey : temra.get(knokey,'') })

    rslib = recomc(keysa,keywo,knolib,unoset,usrid)
    for rskey in rslib:
        for itema in rslib.get(rskey,[]):
            try:
                itema.encode('latin-1')
                finno = finno + "    /rg_"+fsdic[rskey]+"_"+itema+" "+itema+" ("+skdic[rskey]+")\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=itema
                finno = finno + "    /rgs_"+fsdic[rskey]+"_"+numme+str(nodda)+" "+itema+" ("+skdic[rskey]+")\n\n"
                nodda = nodda + 1
    return { 1:finno , 2:conta}

""" mmcdb.listAcc('ch','chu',keywo,chat_id)"""
def listAcc(pref,prefs,keywo,usrid):
    skdic = mmcDefauV.keywo('ssalk')
    sfdic = mmcDefauV.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    #refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['fromm'].keys())+list(libro['key']['toooo'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listSeller(self._temra.get('klass',''),'rg','rgs',keywo,chat_id)"""
def listSeller(klass,pref,prefs,keywo,usrid):
    skdic = mmcDefauV.keywo('ssalk')
    sfdic = mmcDefauV.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0

    rawdb = opendb(usrid).get('raw',{})
    keydb = opendb(usrid).get('key',{})
    listo = []
    for uuid in keydb.get('klass',{}).get(klass,[]):
        listo.append(rawdb.get(uuid,{}).get('shoop',''))
    lists = set(listo)

    for intta in lists:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
            except UnicodeEncodeError:
                conta.update( { numme+str(nodda) : intta })
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+" ("+skdic.get(keywo, skdic.get(sfdic.get(keywo,''),'') )+")\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKas('ch','chu',keywo,chat_id)"""
def listKas(pref,prefs,keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    #refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['klass'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKen('ch','chu',keywo,chat_id)"""
def listKen(pref,prefs,keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    #refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['karen'].keys())+list(libro['key']['tkare'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

def listLigua(pref,keywo,usrid):
    finno = ""
    listo = mmcDefauV.keywo('lingua')
    for intta in listo:
        finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
    return {1:finno,2:{}}

def listList(datte,usrid):
    tasta=""
    try:
        libron = opendb(usrid)
        for n in libron['key']['datte'][datte]:
            tasta = tasta + '/uuid_'+n+'\n    '
            tasta = tasta + libron['raw'][n]['datte']+'  '
            tasta = tasta + libron['raw'][n]['namma']+'  '
            tasta = tasta + libron['raw'][n]['klass']+'  '
            tasta = tasta + libron['raw'][n]['karen']+' '
            tasta = tasta + libron['raw'][n]['price']+'\n'
        return tasta
    except IndexError :
        return ''
