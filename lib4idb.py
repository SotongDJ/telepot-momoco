import json, pprint, tool
# fille = __
# lib4idb.write(fille,'raw',lib4idb.opendb(fille,','))

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
