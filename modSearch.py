import modDatabase, modVariables

def sachi(usrdir,dicto):
    print('modSearch.sachi: '+usrdir)
    libra = modDatabase.opendb(usrdir)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    keywo = dicto.get('keywo','')
    print('keywo: '+keywo)
    dtempo = dicto.get('dtempo','')
    print('dtempo: '+dtempo)
    utempo = dicto.get('utempo','')
    print('utempo: '+utempo)
    cokas = dicto.get('cokas','')
    print('cokas: '+cokas)

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
