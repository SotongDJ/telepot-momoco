from core import modDatabase
from core import tool

def listKeywo(usrdir):
    print('modDatabase.listKeywo: '+tool.mask(usrdir))
    keydb = modDatabase.opendb(usrdir).get('key',{})
    resut = {}
    for kas in keydb.keys():
        if kas not in ['datte','price','tpric','desci','karen','tkare']:
            for keywo in keydb.get(kas,{}).keys():
                numon = 0
                metdi = {}
                metse = []

                metdi = resut.get(keywo,{})
                metse = metdi.get(kas,[])
                metse.extend(keydb.get(kas,{}).get(keywo,[]))
                metdi.update({ kas : metse })
                resut.update({ keywo : metdi })
    return resut

def exper(usrdir,keywo):
    """Grab word from msg"""

    keydb = modDatabase.opendb(usrdir).get('key',{})
    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    kewulista = modDatabase.listKeywo(usrdir)
    # kewulista = {keywo: {class : [ uuid ]}}

    kasdik = {} # {class : [keyword]}
    udilis = [] # [uuid]
    udidik = {} # {uuid : score }
    secodi = {0:[0]} # {score : uuid}

    for keyto in kewulista.keys():
        if keyto in keywo:
            for kasse in kewulista.get(keyto).keys():
                metase = kasdik.get(kasse,[])
                metase.append(keyto)
                kasdik.update({ kasse : metase })
                udilis.extend(kewulista.get(keyto).get(kasse))
    # pprint.pprint(kasdik)
    nummo = 0
    for uuid in udilis:
        nummo = udidik.get(uuid,0)
        nummo = nummo + 1
        udidik.update({ uuid : nummo })

    setta = []
    for uuid in udidik:
        nummo = udidik.get(uuid)
        setta = secodi.get(nummo,[])
        setta.append(uuid)
        secodi.update({ nummo : setta })
    # pprint.pprint(secodi)

    finudi = [] # [uuid]
    fikali = [] # [class]
    fikeli = [] # [keyword]
    fikasi = '' # class-class...
    fudidi = {} # { keywo-keywo... : score}

    kasse = ''
    finudi = secodi.get(max(sorted(list(secodi.keys()))))
    if finudi == [0]:
        return {}
    else:
        fikali = sorted(list(kasdik.keys()))
        # pprint.pprint(fikeli)
        for kasse in fikali:
            if fikasi == "":
                fikasi = kasse
            else:
                fikasi = fikasi + '@' + kasse
        # print("fikasi:"+fikasi)
        for kewoli in kasdik.values():
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

def numof(keywo):
    pre = False
    resut = '0'
    metasi = ''
    metase = []
    numan = ['0','1','2','3','4','5','6','7','8','9']
    nunot = ['.',',']
    for stik in keywo:
        if stik in numan:
            if pre:
                metasi = metasi + stik
            else:
                metasi = stik
            pre = True
        elif stik in nunot:
            if pre:
                metasi = metasi + stik
                pre = True
        else:
            pre = False
            if metasi != '':
                metase.append(metasi)
                metasi = ''
    if pre:
        pre = False
        if metasi != '':
            metase.append(metasi)
            metasi = ''
    # pprint.pprint(metase)

    leva = 0
    for nummo in metase:
        if '.' in nummo:
            if float(nummo.replace(',','')) > float(resut):
                resut = nummo.replace(',','')
                leva = 2
        elif leva <2:
            if float(nummo.replace(',','.')) > float(resut):
                resut = nummo.replace(',','.')
                leva = 1

    if resut == '0':
        resut = ''
    return resut
