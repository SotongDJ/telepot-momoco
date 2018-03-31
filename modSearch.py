from core import modDatabase, tool

import modKeywo, modArgona, pprint

def numof(mesag):
    print('modSearch.numof')
    print('mesag: '+mesag)
    pre = False
    resut = '0'
    metasi = ''
    metase = []
    numan = ['0','1','2','3','4','5','6','7','8','9']
    for stik in mesag:
        if stik == '#':
            if pre:
                metase.append(metasi)
                metasi = ''
            else:
                pre = True
        elif stik in numan:
            if pre:
                metasi = metasi + stik
        elif stik == '-':
            if pre:
                metasi = metasi + stik
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
    metadi = {}
    for numdo in metase:
        if len(numdo) > 10:
            null = metase.pop(metase.index(numdo))
        elif len(numdo) >= 5:
            if numdo[4] != '-':
                null = metase.pop(metase.index(numdo))
            elif len(numdo) >= 8:
                if numdo[7] != '-':
                    null = metase.pop(metase.index(numdo))
    for numdo in metase:
        domun = numdo.replace('-','')
        if len(domun) < 8 :
            domun = domun + '0'*(8-len(domun))
        metadi.update({int(domun):numdo})

    if len(metadi) != 0:
        btempo = metadi.get(min(metadi.keys()))
        ftempo = metadi.get(max(metadi.keys()))
    else:
        btempo = ''
        ftempo = ''

    resut = {
        'datese' : metase,
        'btempo' : btempo,
        'ftempo' : ftempo,
    }
    return resut

def kenwo(mesag):
    metase = []
    defal = modArgona.Argo()
    temran = defal.temra

    mesalista = mesag.split(' ')
    for kasso in set(defal.temra.keys()):
        for mesol in mesalista:
            # print(kasso+" vs. "+mesol)
            if '#'+kasso in mesol:
                keywo = mesol.replace('#'+kasso,'')
                metase.append(mesol)
                # pprint.pprint(metase)
                temran.update({ kasso : keywo })

    for kasso in set(temran.keys()):
        if temran.get(kasso,'') == '':
            null = temran.pop(kasso)

    resut = {
        'ketase':metase,
        'temran':temran,
    }
    return resut

def exper(usrdir,mesag,preudi=[]):
    """Grab word from msg"""
    print('modSearch.exper: '+tool.mask(usrdir))

    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    limit = ['datte']
    kewulista = modKeywo.listKeywo(usrdir,limit=limit)
    # kewulista = {keywo: {class : [ uuid ]}}

    tempo = numof(mesag)
    btempo = tempo.get('btempo','')
    ftempo = tempo.get('ftempo','')
    datese = tempo.get('datese','')
    if preudi == []:
        preudi = modDatabase.timra(usrdir,btempo=btempo,ftempo=ftempo,modde='uuid')
    print('preudi: ' + str(len(preudi)) + ' record(s)')

    kenwon = kenwo(mesag)
    ketase = kenwon.get('ketase',[])
    temran = kenwon.get('temran',{})
    for uuid in preudi:
        tendra = rawdb.get(uuid,{})
        status = False
        for kasso in set(temran.keys()):
            fronto = tendra.get(kasso,'')
            if fronto != temran.get(kasso,0):
                status = True
        if status:
            preudi = list(set(preudi))
            null = preudi.pop(preudi.index(uuid))

    mesalista = mesag.split(' ')
    mesalista = list(set(mesalista+list(temran.values())))
    tratas = list(set(datese+ketase))
    for mesol in mesalista:
        if mesol in tratas:
            null = mesalista.pop(mesalista.index(mesol))
    mesdik = {} # {class : [keyword]}
    udilis = [] # [uuid]
    mesodi = [] # [mesol]

    for keyto in kewulista.keys():
        for mesol in mesalista:
            if mesol in keyto:
                mesodi.append(mesol)
                for kasse in kewulista.get(keyto).keys():
                    metase = mesdik.get(kasse,[])
                    metase.append(keyto)
                    mesdik.update({ kasse : metase })
                    udilis.extend(kewulista.get(keyto).get(kasse))
    # pprint.pprint(mesdik)
    # pprint.pprint(udilis)

    finudi = [] # [uuid]
    fikali = [] # [class]
    fikeli = [] # [keyword]
    fikasi = '' # class-class...
    fudidi = {} # { keywo-keywo... : [uuid]}
    falson = []
    resudi = [] # [uuid] for preudi

    kasse = ''
    finudi = sorted(list(udilis))
    # pprint.pprint(finudi)
    fikali = sorted(list(mesdik.keys()))
    # pprint.pprint(fikali)
    for kewoli in mesdik.values():
        fikeli.extend(kewoli)
    # pprint.pprint(fikeli)
    for kasse in fikali:
        if fikasi == "":
            fikasi = kasse
        else:
            fikasi = fikasi + '@' + kasse
    # print("fikasi:"+fikasi)

    for uuid in finudi:
        if uuid in preudi:
            metasi = ''

            for kasse in fikali:
                keyta = rawdb.get(uuid).get(kasse)

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

            statu = 0
            for mesol in mesodi:
                if mesol in metasi:
                    if statu == 0:
                        statu = 2
                else:
                    if statu == 2:
                        statu = 1
                    elif statu == 0:
                        statu = 1
            if statu == 1:
                falson.append(metasi)
            elif statu == 2:
                metaso = fudidi.get(metasi,[])
                metaso.append(uuid)
                metaso = sorted(list(set(metaso)))
                resudi.append(uuid)
                fudidi.update({ metasi : metaso })
    # pprint.pprint(fudidi)
    falson = sorted(list(set(falson)))
    # pprint.pprint(falson)
    resudi = sorted(list(set(resudi)))
    print('resudi: ' + str(len(resudi)) + ' record(s)')

    resut = {}
    resut.update({ 'fikasi' : fikasi})
    resut.update({ 'fudidi' : fudidi})
    resut.update({ 'resudi' : resudi})

    return resut

def samuk(usrdir,mesag,karen='MYR'):
    trase = exper(usrdir,mesag)
    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    resudi = trase.get('resudi',[])

    gabadi = {}
    for uuid in resudi:
        rawdi = {}
        rawdi.update(rawdb.get(uuid,{}))

        if rawdi.get('tkare') != karen:
            price = modDatabase.cvKaren(usrdir,rawdi.get('tkare'),karen,float(rawdi.get('tpric')))
        else:
            price = float(rawdi.get('tpric'))

        price = round(price,2)

        for kasso in rawdi.keys():
            if kasso not in ['price','tpric','desci']:
                kasdi = {}
                kasdi.update(gabadi.get(kasso,{}))

                keywo = rawdi.get(kasso,'')

                keidi = {}
                keidi.update(kasdi.get(keywo,{}))

                keili = keidi.get('bil',[])
                keili.append(price)

                keidi.update({ 'bil' : keili})

                kasdi.update({ keywo : keidi })

                gabadi.update({ kasso : kasdi })

        for kasso in gabadi.keys():
            kasdi = {}
            kabi = []
            kasdi.update(gabadi.get(kasso))

            for keywo in kasdi.keys():
                keili = {}
                keili.update(kasdi.get(keywo))

                bila = keili.get('bil',[])
                if bila == []:
                    suma = 0.00
                    cint = 0
                    avge = 0.00
                    minu = 0.00
                    maxu = 0.00
                else:
                    suma = round(sum(bila),2)
                    cint = len(bila)
                    avge = round(suma/cint,2)
                    minu = min(bila)
                    maxu = max(bila)
                kabi.append(suma)

                keili.update({
                    'sum' : suma,
                    'cnt' : cint,
                    'avg' : avge,
                    'min' : minu,
                    'max' : maxu,
                })
                kasdi.update({ keywo : keili })

            sama = round(sum(kabi),2)
            cont = len(kabi)
            aveg = round(sama/cont,2)
            mini = min(kabi)
            maxi = max(kabi)
            metadi = {
                'sum' : sama,
                'cnt' : cont,
                'avg' : aveg,
                'min' : mini,
                'max' : maxi,
            }
            kasdi.update({ '@total@' : metadi })
            gabadi.update({ kasso : kasdi })

            for keywo in kasdi.keys():
                keili = {}
                keili.update(kasdi.get(keywo))

                suma = keili.get('sum')
                pcet = int(round( (suma/sama)*100, 0))

                keili.update({'pct' : pcet,})
                kasdi.update({ keywo : keili })

                gabadi.update({ kasso : kasdi })

    return gabadi
