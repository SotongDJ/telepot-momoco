import os
def initisa(modol):
    os.system("mkdir -p ./database/keywo/"+modol)

def dicto(modol):
    dic={}
    for lyne in open("./database/keywo/"+modol+"/dicto").read().splitlines():
        lino=lyne.split(":")
        if float(lino[1])%1 == 0:
            dic[lino[0]]=int(lino[1])
        else:
            dic[lino[0]]=float(lino[1])
    return dic
def dikta(modol):
    dik={}
    for lyne in open("./database/keywo/"+modol+"/dikta").read().splitlines():
        lino=lyne.split(":")
        if float(lino[1])%1 == 0:
            dik[lino[0]]=int(lino[1])
        elif float(lino[1])%1 != 0:
            dik[lino[0]]=float(lino[1])
    return dik
