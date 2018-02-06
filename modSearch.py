from core import modDatabase
from core import tool

import modKeywo,pprint

def exper(usrdir,mesag):
    """Grab word from msg"""
    print('modRecom.exper: '+tool.mask(usrdir))
    keydb = modDatabase.opendb(usrdir).get('key',{})
    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    kewulista = modKeywo.listKeywo(usrdir)
    # kewulista = {keywo: {class : [ uuid ]}}

    mesalista = mesag.split(' ')
    mesdik = {} # {class : [keyword]}
    udilis = [] # [uuid]
    udidik = {} # {uuid : score }
    dikudi = {0:[0]} # {score : uuid}

    for keyto in kewulista.keys():
        if keyto in mesag:
            for kasse in kewulista.get(keyto).keys():
                metase = mesdik.get(kasse,[])
                metase.append(keyto)
                mesdik.update({ kasse : metase })
                udilis.extend(kewulista.get(keyto).get(kasse))
    # pprint.pprint(mesdik)
    nummo = 0
    for uuid in udilis:
        nummo = udidik.get(uuid,0)
        nummo = nummo + 1
        udidik.update({ uuid : nummo })

    setta = []
    for uuid in udidik:
        nummo = udidik.get(uuid)
        setta = dikudi.get(nummo,[])
        setta.append(uuid)
        dikudi.update({ nummo : setta })
    # pprint.pprint(dikudi)

    finudi = [] # [uuid]
    fikali = [] # [class]
    fikeli = [] # [keyword]
    fikasi = '' # class-class...
    fudidi = {} # { keywo-keywo... : score}

    kasse = ''
    finudi = dikudi.get(max(sorted(list(dikudi.keys()))))
    if finudi == [0]:
        return {}
    else:
        fikali = sorted(list(mesdik.keys()))
        # pprint.pprint(fikeli)
        for kasse in fikali:
            if fikasi == "":
                fikasi = kasse
            else:
                fikasi = fikasi + '@' + kasse
        # print("fikasi:"+fikasi)
        for kewoli in mesdik.values():
            fikeli.extend(kewoli)
        nummo = 0
        for uuid in finudi:
            metasi = ''
            for kasse in fikali:
                keyta = rawdb.get(uuid).get(kasse)
                # print("keyta:"+keyta)
                if keyta not in fikeli:
                    keyta = ''
                if metasi == '':
                    if keyta == '':
                        metasi = '@'
                    else:
                        metasi = keyta
                elif metasi == '@':
                    metasi = metasi + keyta
                else:
                    metasi = metasi + '@' + keyta
            nummo = fudidi.get(metasi,0)
            nummo = nummo + 1
            fudidi.update({ metasi : nummo })
        # pprint.pprint(fudidi)

        resudi = {} # { score : last keywo-keywo}
        for metakesi in fudidi.keys():
            sekor = fudidi.get(metakesi)
            resudi.update({ sekor : metakesi })

        resut = {}
        fikesi = resudi.get(max(sorted(list(resudi.keys()))))
        fikase = fikasi.split('@')
        fikese = fikesi.split('@')
        if len(fikase) != len(fikese):
            print("fikasi: "+fikasi)
            print("fikesi: "+fikesi)
            pprint.pprint(fikase)
            pprint.pprint(fikese)
        else:
            for numelo in range(0,len(fikase)):
                if fikese[numelo] != '':
                    resut.update({ fikase[numelo] : fikese[numelo] })
        # pprint.pprint(resut)
        return resut
