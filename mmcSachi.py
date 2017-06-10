import mmcdb, mmcDefauV

def sachi(usrid,dicto):
    libra = mmcdb.opendb(usrid)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    keywo = dicto.get('keywo','')
    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')

    tiset = mmcdb.timra(usrid, dtempo=dtempo, utempo=utempo)

    ralib = {}
    keyra = {}
    for keyo in keydb.keys():
        for valo in keydb.get(keyo).keys():
            vakey = ralib.get(valo,[])
            nonom = len(vakey)
            vaset = keydb.get(keyo).get(valo)
            vakey.extend([x for x in vaset if x in tiset])
            nonam = len(vakey)
            if nonam > nonom:
                ralib.update({ valo : vakey })

                kekey = keyra.get(valo,[])
                kekey.extend([keyo])
                keyra.update({ valo : kekey })

    kelib = {}
    keyto = {}
    for valo in ralib.keys():
        if keywo in valo:
            kelib.update({ valo : ralib.get(valo,[]) })
            keyto.update({ valo : keyra.get(valo,[]) })

    return { 'kelib': kelib , 'keyto': keyto }

def listSachi(usrid,libto,lingua='enMY'):
    libra = mmcdb.opendb(usrid)
    rawdb = libra.get('raw',{})

    kelib = libto.get('kelib',{})
    keyto = libto.get('keyto',{})

    transle = mmcDefauV.keywo('transle',lingua=lingua)
    resut = ''
    for keyo in kelib.keys():
        resut = resut + keyo+ ' (' + ', '.join([transle.get(x,'') for x in keyto.get(keyo,[]) ])+ ') ' + ': \n'
        for uuid in set(kelib.get(keyo,[])):
            resut = resut + '　/uuid_'+uuid+'\n　　'
            resut = resut + rawdb.get(uuid,{}).get('datte','')+'　'
            resut = resut + rawdb.get(uuid,{}).get('namma','')+'　'
            resut = resut + rawdb.get(uuid,{}).get('klass','')+'　'
            resut = resut + rawdb.get(uuid,{}).get('karen','')+' '
            resut = resut + rawdb.get(uuid,{}).get('price','')+'\n'
        resut = resut + '\n'

    return resut
