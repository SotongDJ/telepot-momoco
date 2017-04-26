import json, pprint, tool, random
# fille = __
# mmcdb.writedb(fille,'raw',mmcdb.opencsv(fille,','))

def opendb(fille):
    fit = open(fille,'r')
    libra = json.load(fit)
    return libra

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

def appenddb(fille,keywo,lib):
    filla = open(fille,"r")
    source = json.load(filla)
    filla.close()
    for namma in list(lib.keys()):
        source[keywo][namma]=lib[namma]
    filla = open(fille,"w")
    json.dump(source,filla)
    filla.close()

"""--------------------------------------------------------
        record = mmcdb.addRaw(chat_id,self._temra)
"""
def addRaw(usrid,temra):
    record = {
        'raw':{},
        'key':{}
        }

    try:
        faale = open(tool.path("momoco",usrid)+"record.json","r")
        record = json.load(faale)
        print("Load Old Record")
        faale.close()
    except FileNotFoundError:
        print('FileNotFoundError')

    timta = tool.date(3,'0000')
    record["raw"][timta] = temra
    print("Add Record")
    faale = open(tool.path("momoco",usrid)+"record.json","w")
    json.dump(record,faale)
    faale.close()
    return record

def recoma(keys,libra):
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
    libre = opendb(tool.path("momoco",usrid)+"record.json")
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
        refesKey(tool.path("momoco",chat_id)+"record.json")
"""
def refesKey(fille):
    faale = open(fille,'r')
    libra = json.load(faale)
    libra['key']={}
    for uuid in list(libra['raw'].keys()):
        libra=addKey(uuid,libra['raw'][uuid],'key',libra)
    faale = open(fille,'w')
    json.dump(libra,faale)
    faale.close()
