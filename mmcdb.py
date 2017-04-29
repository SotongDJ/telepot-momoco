import json, random, hashlib
import tool, mmctool
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
        setting = {
            "dinco":"", "dexpe":"",
            "genis":"", "ovede":"",
            "tanfe":"", "incom":""
        }
        return setting

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

""" addKey(uuid,libra) """
def addKey(ketta,libra,usrid):
    pri="inti : "
    for setta in list(libra['raw'][ketta].keys()):
        try:
            if libra['key'][setta] == {}:
                pri=pri+"key>blank,"
            else:
                pri=pri+"key>exist,"
        except KeyError:
            libra['key'][setta]={}
            pri=pri+"key>create,"

        try:
            if libra['key'][setta][libra['raw'][ketta][setta]] == []:
                pri=pri+"crosskey>blank,"
            else:
                pri=pri+"crosskey>exist,"
        except KeyError:
            libra['key'][setta][libra['raw'][ketta][setta]] = []
            pri=pri+"crosskey>create,"

        if libra['raw'][ketta][setta] != "":
            if libra['key'][setta][libra['raw'][ketta][setta]] != []:
                libra['key'][setta][libra['raw'][ketta][setta]].append(ketta)
            else:
                libra['key'][setta][libra['raw'][ketta][setta]]=[ketta]
        pri=pri+". "
    mmctool.printbug('addkey\n    pri',pri,usrid)
    return libra

""" addHash(libra)"""
def addHash(libra):
    for uuid in list(libra['raw'].keys()):
        hasa = hashlib.sha512()
        if libra['raw'][uuid] != {}:
            hasa.update((",".join(set(list(libra['raw'][uuid].values())))).encode("utf-8"))
            libra['hash'][uuid] = hasa.hexdigest()
    return libra

""" fixAcc(libra[raw],usrid)"""
def fixAcc(liboh,usrid):
    setti = openSetting(usrid)
    for sekio in list(liboh.keys()):
        if liboh[sekio] != {}:
            try:
                if liboh[sekio]['fromm'] == "":
                    liboh[sekio]['fromm'] = setti['genis']
            except KeyError:
                liboh[sekio]['fromm'] = setti['genis']

            try:
                if liboh[sekio]['toooo'] == "":
                    liboh[sekio]['toooo'] = setti['ovede']
            except KeyError:
                liboh[sekio]['toooo'] = setti['ovede']

            try:
                if liboh[sekio]['tpric'] == "":
                    liboh[sekio]['tpric'] = liboh[sekio]['price']
            except KeyError:
                try:
                    if liboh[sekio]['price'] == "":
                        liboh[sekio]['tpric'] = "0"
                        liboh[sekio]['price'] = "0"
                    else:
                        liboh[sekio]['tpric'] = liboh[sekio]['price']
                except KeyError:
                    liboh[sekio]['tpric'] = "0"
                    liboh[sekio]['price'] = "0"

    return liboh

""" mmcdb.refesdb(chat_id)"""
def refesdb(usrid):
    libra = opendb(usrid)
    libra['raw']=fixAcc(libra['raw'],usrid)
    libra['key']={}
    libra['hash']={}
    for uuid in list(libra['raw'].keys()):
        libra=addKey(uuid,libra,usrid)
    libra=addHash(libra)
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

""" appendRaw(usrid,lib)"""
def appendRaw(usrid,lib):
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
    refesdb(usrid)
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

""" mmcdb.recomtxt(self._temra,self._keys,self._keywo,['namma','klass','shoop','price'],self._fs,chat_id) """
def recomtxt(temra,keysa,keywo,deset,fsdic,usrid):
    setto = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    for deskey in deset:
        mmctool.printbug('temra[deskey]',temra[deskey],usrid)
        if temra[deskey] == "":
            setto = recomb(keysa,keywo,deskey,usrid)
            mmctool.printbug('setto',setto,usrid)
            if setto != []:
                for itema in setto:
                    try:
                        itema.encode('latin-1')
                        finno = finno + "    /rg_"+fsdic[deskey]+"_"+itema+"\n"
                    except UnicodeEncodeError:
                        conta[numme+str(nodda)]=itema
                        finno = finno + "    /rgs_"+fsdic[deskey]+"_"+numme+str(nodda)+" "+itema+"\n"
                        nodda = nodda + 1
                # old time :rgkey=" /rg_"+fsdic[deskey]+"_"
                #           finno=finno+rgkey+rgkey.join(setto)+"\n"
    return { 1:finno , 2:conta}

""" mmcdb.listAcc('ch','chu',keywo,chat_id)"""
def listAcc(pref,prefs,keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['fromm'].keys())+list(libro['key']['toooo'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+"\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKas('ch','chu',keywo,chat_id)"""
def listKas(pref,prefs,keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(100,1000)))
    nodda = 0
    refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['klass'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+"\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

""" mmcdb.listKen('ch','chu',keywo,chat_id)"""
def listKen(pref,prefs,keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    refesdb(usrid)
    libro = opendb(usrid)
    listo = set(list(libro['key']['karen'].keys())+list(libro['key']['tkare'].keys()))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /"+pref+"_"+keywo+"_"+intta+"\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /"+prefs+"_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

def changeSetting(libra,usrid):
    faale = open(tool.path("momoco",usrid)+"setting.json",'w')
    json.dump(libra,faale)
    faale.close()
