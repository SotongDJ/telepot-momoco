import modDatabase, modVariables

def sachi(usrdir,dicto):
    print('modSearch.sachi: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    keywo = dicto.get('keywo','')
    dtempo = dicto.get('dtempo','')
    utempo = dicto.get('utempo','')
    cokas = dicto.get('cokas','')

    tiset = modDatabase.timra(usrdir, dtempo=dtempo, utempo=utempo)

    if cokas == '':
        kaset = keydb.keys()
    else:
        kaset = [cokas]

    ralib = {}
    keyra = {}
    for keyo in kaset:
        for valo in keydb.get(keyo,{}).keys():
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

    kelib = {} # searchresut : uuid
    keyto = {} # searchresut : class
    for valo in ralib.keys():
        if keywo in valo:
            kelib.update({ valo : ralib.get(valo,[]) })
            keyto.update({ valo : keyra.get(valo,[]) })

    return { 'kelib': kelib , 'keyto': keyto }

def listSachi(usrdir,libto,lingua='enMY'):
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})

    kelib = libto.get('kelib',{})
    keyto = libto.get('keyto',{})

    transle = modVariables.keywo('transle',lingua=lingua)
    resut = {'resut':{},'lenam':1,'lenes':1}

    lenam = 1
    lenes = 1
    for keyo in kelib.keys():
        conto = []
        namma = keyo + '\n'
        lenna = len(namma)
        if lenam < lenna:
            lenam = lenna
        otnoc = [transle.get(x,'') for x in keyto.get(keyo,[]) ]
        namma = namma +'(' + ',\n'.join(otnoc)+ ')'
        masio = max(otnoc, key=len)
        if lenam < len(masio):
            lenam = len(masio)
        for uuid in set(kelib.get(keyo,[])):
            testa = 'uuid:'+ uuid +'　'
            testa = testa + rawdb.get(uuid,{}).get('datte','')+'\n'
            lenta = len(testa)
            if lenes < lenta:
                lenes = lenta
            testa = testa + rawdb.get(uuid,{}).get('namma','')+'　'
            testa = testa + rawdb.get(uuid,{}).get('shoop','')+'　'
            testa = testa + rawdb.get(uuid,{}).get('klass','')+'\n'
            if lenes < len(testa) - lenta:
                lenes = len(testa) - lenta
            lenta = len(testa) - lenta
            testa = testa + rawdb.get(uuid,{}).get('karen','')+' '
            testa = testa + rawdb.get(uuid,{}).get('price','')
            if lenes < len(testa)-lenta:
                lenes = len(testa)-lenta
            conto.append(testa)
        resut.get('resut').update({ namma : conto })
    resut.update({'lenam':lenam})
    resut.update({'lenes':lenes})

    return resut
