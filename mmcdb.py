import json, pprint, tool, random
# fille = __
# mmcdb.writedb(fille,'raw',mmcdb.opencsv(fille,','))

def opendb(usrid):
    try:
        faale = open(tool.path("momoco",usrid)+"record.json","r")
        record = json.load(faale)
        print("Load Record")
        faale.close()
        return record
    except FileNotFoundError:
        print('FileNotFoundError')
        return {'raw':{},'key':{}}

def openSetting(usrid):
    try:
        faale = open(tool.path("momoco",usrid)+"setting.json","r")
        setting = json.load(faale)
        print("Load Setting")
        faale.close()
        return setting
    except FileNotFoundError:
        print('FileNotFoundError')
        setting = {
            "dinco":"", "dexpe":"",
            "genis":"", "ovede":"",
        }
        return setting

def opencsv(fille,keywo):
    result = {}
    numo = 0
    for linne in open(fille).read().splitlines():
        if "!" in linne:
            keys = linne.replace("!","").split(keywo)
        elif "#" not in linne:
            zero = '9000'
            uri = tool.date(3,'')
            nama = uri+zero[0:4-len(str(numo))]+str(numo)
            result[nama]={}
            word = linne.split(keywo)
            for n in range(0,len(word)):
                result[nama][keys[n]]=word[n]
            numo = numo + 1
    return result

def appendRaw(usrid,lib):
    filla = open(tool.path("momoco",usrid)+"record.json","r")
    source = json.load(filla)
    filla.close()
    for namma in list(lib.keys()):
        source['raw'][namma]=lib[namma]
    filla = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(source,filla)
    filla.close()

"""--------------------------------------------------------
        record = mmcdb.addRaw(chat_id,self._temra)
"""
def addRaw(usrid,temra):
    record = opendb(usrid)
    timta = tool.date(3,'0000')
    record["raw"][timta] = temra
    print("Add Record")
    faale = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(record,faale)
    faale.close()
    return record

def addKey(ketta,seque,desti,libra):
    pri="start:"
    for setta in list(seque.keys()):
        try:
            if libra[desti] == {}:
                pri=pri+"a-"
            else:
                pri=pri+"a+"
        except KeyError:
            libra[desti] = {}

        try:
            if libra[desti][setta] == {}:
                pri=pri+"b-"
            else:
                pri=pri+"b+"
        except KeyError:
            libra[desti][setta]={}

        try:
            if libra[desti][setta][seque[setta]] == []:
                pri=pri+"c-"
            else:
                pri=pri+"c+"
        except KeyError:
            libra[desti][setta][seque[setta]] = []

        if seque[setta] != "":
            if libra[desti][setta][seque[setta]] != []:
                libra[desti][setta][seque[setta]].append(ketta)
            else:
                libra[desti][setta][seque[setta]]=[ketta]
        pri=pri+"  "
    print(pri)
    return libra

"""--------------------------------------------------------
        mmcdb.refesKey(chat_id)
"""
def refesKey(usrid):
    libra = opendb(usrid)
    libra['key']={}
    for uuid in list(libra['raw'].keys()):
        libra=addKey(uuid,libra['raw'][uuid],'key',libra)
    faale = open(tool.path("momoco",usrid)+"record.json",'w')
    json.dump(libra,faale)
    faale.close()


def recoma(keys,usrid):
    refesKey(usrid)
    libra = opendb(usrid)
    listo = []
    try:
        for veluo in list(libra[keys].keys()):
            for uuid in libra[keys][veluo]:
                listo.append(veluo)
    except KeyError:
        print("KeyError")
    lista = []
    setto = set(listo)
    for n in [1,2,3,4,5]:
        try:
            dan = max(setto,key=listo.count)
            lista.append(dan)
            setto.remove(dan)
        except ValueError:
            print("No keywo")
    return lista

def recomb(srckey,veluo,deskey,usrid):
    refesKey(usrid)
    libre = opendb(usrid)
    listo = []
    try:
        for uuid in libre['key'][srckey][veluo]:
            listo.append(libre['raw'][uuid][deskey])
    except KeyError:
        print("KeyError")
    lista = []
    setto = set(listo)
    for n in [1,2,3,4]:
        try:
            dan = max(setto,key=listo.count)
            lista.append(dan)
            setto.remove(dan)
        except ValueError:
            print("No keywo")
    return lista

def recomtxt(temra,keysa,keywo,deset,fsdic,usrid):
    setto = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    for deskey in deset:
        print('temra[deskey] = '+temra[deskey])
        if temra[deskey] == "":
            setto = recomb(keysa,keywo,deskey,usrid)
            pprint.pprint(setto)
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

"""--------------------------------------------------------
        listAcc(keywo,chat_id)
"""
def listAcc(keywo,usrid):
    listo = []
    finno = ""
    conta = {}
    numme = str(random.choice(range(10,100)))
    nodda = 0
    refesKey(usrid)
    libro = opendb(usrid)
    listo = list(set(list(libro['key']['fromm'].keys())+list(libro['key']['toooo'].keys())))
    for intta in listo:
        if intta != '':
            try:
                intta.encode('latin-1')
                finno = finno + "    /ch_"+keywo+"_"+intta+"\n"
            except UnicodeEncodeError:
                conta[numme+str(nodda)]=intta
                finno = finno + "    /chu_"+keywo+"_"+numme+str(nodda)+" "+intta+"\n"
                nodda = nodda + 1
    return {1:finno,2:conta}

def refesSetting(libra,usrid):
    faale = open(tool.path("momoco",usrid)+"setting.json",'w')
    json.dump(libra,faale)
    faale.close()
