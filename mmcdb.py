import json, pprint, tool
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

def writedb(fille,keywo,lib):
    filla = open(fille,"r")
    source = json.load(filla)
    filla.close()
    for namma in list(lib.keys()):
        source[keywo][namma]=lib[namma]
    filla = open(fille,"w")
    json.dump(source,filla)
    filla.close()

def recom(keys,libra):
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
#def refesRan():

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

def refesKey(fille):
    faale = open(fille,'r')
    libra = json.load(faale)
    libra['key']={}
    for uuid in list(libra['raw'].keys()):
        libra=addKey(uuid,libra['raw'][uuid],'key',libra)
    return libra
