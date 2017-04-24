import json, pprint, tool
# fille = __
# mmcdb.write(fille,'raw',mmcdb.opendb(fille,','))

def opendb(fille,keywo):
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

#def refesRan():

#def refesKey():

def addKey(ketta,seque,rangs,desti,libra):
    for setta in rangs:
        try:
            if libra[desti] == {}:
                print('a-')
            else:
                print('a+')
        except KeyError:
            libra[desti] = {}

        try:
            if libra[desti][setta] == {}:
                print('b-')
            else:
                print('b+')
        except KeyError:
            libra[desti][setta]={}

        try:
            if libra[desti][setta][seque[setta]] == []:
                print('c-')
            else:
                print('c+')
        except KeyError:
            libra[desti][setta][seque[setta]] = []

        if seque[setta] != "":
            if libra[desti][setta][seque[setta]] != []:
                libra[desti][setta][seque[setta]].append(ketta)
            else:
                libra[desti][setta][seque[setta]]=[ketta]
    return libra
