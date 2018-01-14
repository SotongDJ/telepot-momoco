import json, random, hashlib, pprint, requests
import tool, modVariables

def opendb(usrdir):
    print('modDatabase.opendb: '+usrdir)
    try:
        faale = open(usrdir + '/record.json','r')
        record = json.load(faale)
        faale.close()
        return record
    except FileNotFoundError:
        faale = open(usrdir + '/record.json','w')
        db = {'raw':{},'key':{}}
        json.dump(db,faale,indent=4,sort_keys=True)
        faale.close()
        return db

def openSetting(usrdir):
    print('modDatabase.openSetting: '+usrdir)
    try:
        faale = open(usrdir + '/setting.json','r')
        setting = json.load(faale)
        faale.close()
        return setting
    except FileNotFoundError:
        faale = open(usrdir + '/setting.json','w')
        setting = modVariables.keywo('setting')
        json.dump(setting,faale,indent=4,sort_keys=True)
        faale.close()
        return setting

def changeSetting(usrdir,libra):
    print('modDatabase.changeSetting: '+usrdir)
    faale = open(usrdir + '/setting.json','w')
    json.dump(libra,faale,indent=4,sort_keys=True)
    faale.close()

def openKaratio(usrdir):
    print('modDatabase.openKaratio: '+usrdir)
    tool.ckfile(usrdir,'karen.json',addi='json')
    faale = open(usrdir + '/karen.json',"r")
    try:
        karatio = json.load(faale)
    except ValueError:
        karatio = {}
    faale.close()
    return karatio

def getKaratio(usrdir,keydb,modde='refes'):
    print('modDatabase.getKaratio: '+ usrdir)
    print('modde: '+modde)
    resut = False
    if int(tool.acedate(usrdir,'karen')) < int(tool.date()):
        if modde == 'refes':
            karatio = openKaratio(usrdir)
        elif modde == 'reset':
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

        faale = open(usrdir + '/karen.json',"w")
        json.dump(karatio,faale,indent=4,sort_keys=True)
        tool.acedate(usrdir,'karen',modda='write')
        faale.close()

        resut = True
    return resut

def opencsv(fille,keywo):
    print('modDatabase.opencsv')
    print('keywo: '+keywo)
    result = {}
    numo = 0
    for linne in open(fille,'br').read().decode('utf-8').splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        elif linne[0] != "#":
            zero = '9000'
            uri = tool.date(modde=3)
            nama = uri + zero[ 0 : 4-len(str(numo)) ] + str(numo)
            result.update({ nama : {} })
            word = linne.split(keywo)
            for n in range(0,len(word)):
                result.get(nama,{}).update({ keys[n] : word[n] })
            numo = numo + 1
    return result

def addRaw(usrdir,temra):
    print('modDatabase.addRaw: '+usrdir)
    record = opendb(usrdir)
    timta = tool.date(3) + '0000'
    record.get('raw',{}).update({ timta : temra })
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale,indent=4,sort_keys=True)
    faale.close()
    return record

def chRaw(usrdir,uuid,temra):
    print('modDatabase.chRaw: '+usrdir)
    print('uuid: '+uuid)
    record = opendb(usrdir)
    record.get('raw',{}).update( { uuid : temra } )
    faale = open(usrdir + '/record.json','w')
    json.dump(record,faale,indent=4,sort_keys=True)
    faale.close()
    return record

def diffdb(a,b):
    print('modDatabase.diffdb')
    resut=[]
    for m in a.keys():
        if a.get(m,{}) != b.get(m,{}):
            c=a.get(m,{})
            d=b.get(m,{})
            resut.append([c,d])
    return resut

def genKey(rawdb):
    print('modDatabase.genKey')
    keydb = {}
    eledb = {}
    valudb = {}
    for uuid in rawdb.keys():
        for eleme in rawdb.get(uuid,{}):
            valuh = rawdb.get(uuid,{}).get(eleme,'')
            if valuh != '':
                tadd = eledb.get(eleme,{})

                mobb = tadd.get(valuh,[])
                mobb.append(uuid)
                mobb = sorted(list(set(mobb)))

                tadd.update( { valuh : mobb } )
                eledb.update({ eleme : tadd })
    return eledb

def genHash(rawdb):
    print('modDatabase.genHash')
    hashdb = {}
    for uuid in list(rawdb.keys()):
        hasa = hashlib.sha512()
        if rawdb.get(uuid,{}) != {}:
            hasa.update((",".join(set(list(rawdb.get(uuid,{}).values())))).encode("utf-8"))
            hashdb.update( { uuid : hasa.hexdigest() } )
    return hashdb

def ckrpt(h):
    print('modDatabase.ckrpt')
    l={}
    for n in h.keys():
        if '' in h[n].values():
            for m in h[n].keys():
                if m != 'desci':
                    if h[n][m] == '':
                        l.update( { n : m } )
    return l

def ckdb(a,b):
    print('modDatabase.ckdb')
    l={}
    for uuid in a:
        for n in a[uuid]:
            if n != '':
                if a[uuid][n] !=  b.get(uuid,{}).get(n,''):
                    l.update( { uuid+' '+n  : [a[uuid][n], b.get(uuid,{}).get(n,'')] } )
    return l

def fixAcc(usrdir,rawdb):
    print('modDatabase.fixAcc: '+usrdir)
    setti = openSetting(usrdir)
    #rawdb = opendb(usrid).get('raw',{})

    tanfe = setti.get('tanfe','Transfer')
    incom = setti.get('incom','Income')

    dinco = setti.get('dinco','Bank')
    dexpe = setti.get('dexpe','Cash')
    genis = setti.get('genis','Income')
    ovede = setti.get('ovede','Expense')

    karen = setti.get('karen','')

    for n in list(rawdb):
        ndb = rawdb.get(n,{})
        if ndb.get('klass','') == incom:
            if ndb.get('price','') == '':
                ndb.update( {'price' : ndb.get('tpric','') })
            if ndb.get('karen','') == '':
                ndb.update( {'karen' : ndb.get('tkare','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : genis })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : dinco })
        elif ndb.get('klass','') in tanfe:
            if ndb.get('tpric','') == '':
                ndb.update( {'tpric' : ndb.get('price','') })
            if ndb.get('tkare','') == '':
                ndb.update( {'tkare' : ndb.get('karen','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : dinco })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : dexpe })
        else:
            ndb.update( {'tpric' : ndb.get('price','') })
            ndb.update( {'tkare' : ndb.get('karen','') })
            if ndb.get('fromm','') == '':
                ndb.update( {'fromm' : dexpe })
            if ndb.get('toooo','') == '':
                ndb.update( {'toooo' : ovede })
        rawdb.update({ n : ndb })
    return rawdb

def refesdb(usrdir):
    print('modDatabase.refesdb: '+usrdir)
    libra = {}
    rawdb = opendb(usrdir).get('raw',{})
    rawdb = fixAcc(usrdir,rawdb)
    libra.update( {'raw' : rawdb})
    keydb = genKey(rawdb)
    libra.update( {'key' : keydb})
    faale = open(usrdir + '/record.json','w')
    json.dump(libra,faale,indent=4,sort_keys=True)
    faale.close()

def upgradeSetting(usrdir,lib):
    print('modDatabase.upgradeSetting: '+usrdir)
    libra = openSetting(usrdir)
    if set(libra.keys()) == set(lib.keys()):
        return libra
    else:
        for keywo in libra.keys():
            lib[keywo]=libra[keywo]
        changeSetting(usrdir,lib)
        return lib

def importRaw(usrdir,lib):
    print('modDatabase.importRaw: '+usrdir)
    refesdb(usrdir)
    lib=fixAcc(usrdir,lib)
    source = opendb(usrdir)
    for uuid in list(lib.keys()):
        tasno = 0
        for valvu in lib.get(uuid,{}).keys():
            if valvu not in list(source.get('key',{}).keys()):
                tasno = 1
                print('tasno = 1: lib-'+valvu)
        if tasno == 0:
            hasa = hashlib.sha512()
            if lib[uuid] != {}:
                hasa.update((",".join(set(list(lib[uuid].values())))).encode("utf-8"))
                if hasa.hexdigest() not in genHash(source.get('raw',{})).values():
                    source.get('raw',{}).update({ uuid : lib.get(uuid,{}) })
                    print('Imported: '+uuid+'(uuid)')
                else:
                    print('hasa: same hash already exist')
            else:
                print("hasa: lib[uuid] = {}")
        else:
            print('tasno != 0: '+uuid+'(uuid)')
    filla = open(usrdir + '/record.json','w')
    json.dump(source,filla,indent=4,sort_keys=True)
    filla.close()

def expocsv(usrdir,keywo):
    print('modDatabase.opencsv')
    result = {}
    numo = 0
    temla = usrdir + '/template.csv'
    resuf = open(usrdir + '/result-' + tool.date(3) + '.csv','w')
    rawdb = opendb(usrdir).get('raw')
    for linne in open(temla,'br').read().decode('utf-8').splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        resuf.write(linne + '\n')
    for uuid in sorted(list(rawdb.keys())):
        linno = ''
        temra = rawdb.get(uuid,{})
        for keyso in keys:
            linno = linno + temra.get(keyso,'').replace('\n',' ').replace(keywo,'-') + keywo
        resuf.write(linno+'\n')
    resuf.close()

""" recomc(self._keys,self._keywo,knolib,unoset,usrid) """
def recomc(usrdir,srckey,veluo,knolib,unoset):
    print('modDatabase.recomc: '+usrdir)

    rawdb = opendb(usrdir).get('raw',{})
    keydb = opendb(usrdir).get('key',{})
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
                print('finish listing')
        rslib.update({ rskey : lista })
    return rslib

""" mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],chat_id) """
def recomtxt(usrdir,temra,vetco,keysa,keywo,deset):
    print('modDatabase.recomtxt: '+usrdir)
    fsdic = modVariables.keywo('fs')
    skdic = modVariables.keywo('transle')

    finno = ""
    conta = vetco.get(2,{})
    numme = str(random.choice(range(10,100)))
    nodda = 0

    knolib = {}
    knoset = [ x for x in deset if temra.get(x,'') != '' ]
    unoset = set(deset) - set(knoset)

    for knokey in knoset:
        knolib.update({ knokey : temra.get(knokey,'') })

    rslib = recomc(usrdir,keysa,keywo,knolib,unoset)
    for rskey in rslib:
        for itema in rslib.get(rskey,[]):
            try:
                itema.encode('latin-1')
                finno = finno + "    /rg_"+fsdic[rskey]+"_"+itema+" "+itema+" ("+skdic[rskey]+")\n\n"
            except UnicodeEncodeError:
                conta.update({ numme+str(nodda) : itema })
                finno = finno + "    /rgs_"+fsdic[rskey]+"_"+numme+str(nodda)+" "+itema+" ("+skdic[rskey]+")\n\n"
                nodda = nodda + 1

    return { 1:finno , 2:conta}

def listAcc(usrdir,pref,prefs,keywo):
    print('modDatabase.listAcc: '+usrdir)
    print('pref: '+pref)
    print('prefs: '+prefs)
    print('keywo: '+keywo)
    skdic = modVariables.keywo('transle')
    sfdic = modVariables.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    frodb = keydb.get('fromm',{})
    toodb = keydb.get('toooo',{})
    listo = set(list(frodb.keys())+list(toodb.keys()))
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

def listSeller(usrdir,klass,pref,prefs,keywo):
    print('modDatabase.listSeller: '+usrdir)
    print('klass: '+klass)
    print('pref: '+pref)
    print('prefs: '+prefs)
    print('keywo: '+keywo)
    skdic = modVariables.keywo('transle')
    sfdic = modVariables.keywo('sf')
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0

    rawdb = opendb(usrdir).get('raw',{})
    keydb = opendb(usrdir).get('key',{})
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

def listKas(usrdir,pref,prefs,keywo):
    print('modDatabase.listKas: '+usrdir)
    print('pref: '+pref)
    print('prefs: '+prefs)
    print('keywo: '+keywo)
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    kladb = keydb.get('klass',{})
    listo = set(list(kladb.keys()))
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

def listKen(usrdir,pref,prefs,keywo):
    print('modDatabase.listKen: '+usrdir)
    print('pref: '+pref)
    print('prefs: '+prefs)
    print('keywo: '+keywo)
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    libro = opendb(usrdir)
    keydb = libro.get('key',{})
    kardb = keydb.get('karen',{})
    takdb = keydb.get('tkare',{})
    listo = set(list(kardb.keys())+list(takdb.keys()))
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

def listLigua(pref,keywo):
    print('modDatabase.listLigua')
    print('pref: '+pref)
    print('keywo: '+keywo)
    finno = ""
    listo = modVariables.keywo('lingua')
    for intta in listo:
        finno = finno + "    /"+pref+"_"+keywo+"_"+intta+" "+intta+"\n\n"
    return {1:finno,2:{}}

def listList(usrdir,datte):
    print('modDatabase.listList: '+usrdir)
    print('datte: '+datte)
    tasta=""
    try:
        libron = opendb(usrdir)
        rauron = libron.get('raw',{})
        datron = libron.get('key',{}).get('datte',{}).get(datte,{})
        for n in datron:
            nron = rauron.get(n,{})
            tasta = tasta + '/uuid_'+n+'\n    '
            tasta = tasta + nron.get('datte','') +'  '
            tasta = tasta + nron.get('namma','') +'  '
            tasta = tasta + nron.get('klass','') +'  '
            tasta = tasta + nron.get('karen','') +' '
            tasta = tasta + nron.get('price','') +'\n'
        return tasta
    except IndexError :
        return ''

def timra(usrdir, btempo='',ftempo='', modde='uuid'):
    print('modDatabase.timra: '+usrdir)
    print('modde: '+modde)
    libra = opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    if btempo == '':
        btempo = tool.date(modde=1)[0:7]
    if ftempo == '':
        ftempo = tool.date(modde=1)[0:7]

    ddalit = '0000-00-00'
    udalit = '9999-99-99'
    btempo = btempo + ddalit[len(btempo):len(ddalit)+1]
    ftempo = ftempo + udalit[len(ftempo):len(udalit)+1]
    print('btempo: '+btempo)
    print('ftempo: '+ftempo)

    tok = []
    tak = list(keydb.get('datte',{}).keys())
    tak.append(btempo)
    tak.append(ftempo)
    tik = sorted(set(tak))
    print('datte : '+pprint.pformat(tik,compact=True))

    if tik.index(ftempo)-tik.index(btempo) < 0:
        dlit = ftempo
        ulit = btempo
    else:
        dlit = btempo
        ulit = ftempo

    tuk = tik[tik.index(dlit):tik.index(ulit)+1]

    datui = []
    for datte in tuk:
        datui.extend(keydb.get('datte',{}).get(datte,[]))

    if modde == 'datte':
        return tuk
    elif modde == 'uuid':
        return datui
