from core import modDatabase
from core import tool

import modKeywo,pprint

def exper(usrdir,mesag,btempo='',ftempo=''):
    """Grab word from msg"""
    print('modRecom.exper: '+tool.mask(usrdir))
    datte = modDatabase.timra(usrdir,btempo=btempo,ftempo=ftempo,modde='uuid')
    rawdb = modDatabase.opendb(usrdir).get('raw',{})
    kewulista = modKeywo.listKeywo(usrdir)
    # kewulista = {keywo: {class : [ uuid ]}}

    mesalista = mesag.split(' ')
    mesdik = {} # {class : [keyword]}
    udilis = [] # [uuid]

    for keyto in kewulista.keys():
        for mesol in mesalista:
            if mesol in keyto:
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
        if uuid in datte:
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
            for mesol in mesalista:
                if mesol in metasi:
                    if statu == 0:
                        statu = 2
                else:
                    if statu == 2:
                        statu = 1
                    elif statu == 0:
                        statu = 1
            if statu == 2:
                metaso = fudidi.get(metasi,[])
                metaso.append(uuid)
                fudidi.update({ metasi : metaso })
    # pprint.pprint(fudidi)

    resut = {}
    resut.update({ 'fikasi' : fikasi})
    resut.update({ 'fudidi' : fudidi})

    return resut
