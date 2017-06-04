import mmcDefauV, mmctool, pprint
def chooseMode(ligua):
    final = open('descrimmc/'+ligua+'/analiChoose.descri').read()
    return final

def abratioMain(ligua,dicto):
    final = open('descrimmc/'+ligua+'/abratioMain.descri').read()
    final = final.replace('@mode@',mmctool.ul(dicto.get('mode','')))
    final = final.replace('@dtempo@',mmctool.ul(dicto.get('dtempo','')))
    final = final.replace('@utempo@',mmctool.ul(dicto.get('utempo','')))
    final = final.replace('@conde@',mmctool.ul(dicto.get('conde','')))
    final = final.replace('@conda@',mmctool.ul(dicto.get('conda','')))
    final = final.replace('@targe@',mmctool.ul(dicto.get('targe','')))
    return final

def abratioKeywo(ligua,keywo):
    final = open('descrimmc/'+ligua+'/abratioKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def abratioResut(ligua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    dtempo = resut.get('dtempo','')
    utempo = resut.get('utempo','')
    conda = resut.get('conda','')
    conde = resut.get('conde','')
    targe = resut.get('targe','')
    pri = resut.get('pri',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    par = resut.get('par','')
    kub = resut.get('kub','')
    statik = resut.get('statik','')

    skdic = mmcDefauV.keywo('ssalk')

    a = open('descrimmc/'+ligua+'/abratioResutA.descri').read()
    a = a.replace('@dtempo@',dtempo)
    a = a.replace('@utempo@',utempo)
    a = a.replace('@conde@',conde)
    a = a.replace('@conda@',skdic.get(conda,''))
    a = a.replace('@targe@',skdic.get(targe,''))

    b = open('descrimmc/'+ligua+'/abratioResutB.descri').read()
    b = b.replace('@pri@','\n'.join(pri))
    b = b.replace('@des@',des)
    b = b.replace('@karen@',karen)
    b = b.replace('@sam@',sam)
    b = b.replace('@par@',par)
    b = b.replace('@kub@',kub)

    c = open('descrimmc/'+ligua+'/abratioResutC.descri').read()
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@karen@',karen)
    c = c.replace('@maxPc@',statik.get('maxPc',''))
    c = c.replace('@max@',statik.get('max',''))
    c = c.replace('@min@',statik.get('min',''))
    c = c.replace('@minPc@',statik.get('minPc',''))
    c = c.replace('@time@',statik.get('time',''))
    c = c.replace('@dafro@',statik.get('dafro',''))

    return [a,b,c]

def atrenMain(ligua,dicto):
    ledic=mmcDefauV.keywo('leve')
    final = open('descrimmc/'+ligua+'/atrenMain.descri').read()
    final = final.replace('@mode@',mmctool.ul(dicto.get('mode','')))
    final = final.replace('@dtempo@',mmctool.ul(dicto.get('dtempo','')))
    final = final.replace('@utempo@',mmctool.ul(dicto.get('utempo','')))
    final = final.replace('@conde@',mmctool.ul(dicto.get('conde','')))
    final = final.replace('@conda@',mmctool.ul(dicto.get('conda','')))
    final = final.replace('@leve@',mmctool.ul(ledic.get(dicto.get('leve',10),'')))
    return final

def atrenKeywo(ligua,keywo):
    final = open('descrimmc/'+ligua+'/atrenKeywo.descri').read()
    final = final.replace('@keywo@',keywo)
    return final

def atrenResut(ligua,resut):
    print('resut : '+pprint.pformat(resut, compact=True))

    dtempo = resut.get('dtempo','')
    utempo = resut.get('utempo','')
    conda = resut.get('conda','')
    conde = resut.get('conde','')
    graf = resut.get('graf',[])
    des = resut.get('des','')
    karen = resut.get('karen','')
    sam = resut.get('sam','')
    vam = resut.get('vam','')
    san = resut.get('san','')
    van = resut.get('van','')
    statik = resut.get('statik','')

    skdic = mmcDefauV.keywo('ssalk')

    a = open('descrimmc/'+ligua+'/atrenResutA.descri').read()
    a = a.replace('@dtempo@',dtempo)
    a = a.replace('@utempo@',utempo)
    a = a.replace('@conde@',conde)
    a = a.replace('@conda@',skdic.get(conda,''))

    b = open('descrimmc/'+ligua+'/atrenResutB.descri').read()
    b = b.replace('@graf@','\n'.join(graf))
    b = b.replace('@des@',des)
    b = b.replace('@karen@',karen)
    b = b.replace('@sam@',str(sam))

    c = open('descrimmc/'+ligua+'/atrenResutC.descri').read()
    c = c.replace('@karen@',karen)
    c = c.replace('@sam@',str(sam))
    c = c.replace('@san@',str(san))
    c = c.replace('@vam@',str(vam))
    c = c.replace('@van@',str(van))
    c = c.replace('@sinMax@',statik.get('sinMax',''))
    c = c.replace('@sinMaxPc@',statik.get('sinMaxPc',''))
    c = c.replace('@sinMin@',statik.get('sinMin',''))
    c = c.replace('@sinMinPc@',statik.get('sinMinPc',''))
    c = c.replace('@oveMaxPc@',statik.get('oveMaxPc',''))
    c = c.replace('@oveMaxDat@',statik.get('oveMaxDat',''))
    c = c.replace('@oveMinPc@',statik.get('oveMinPc',''))
    c = c.replace('@oveMinDat@',statik.get('oveMinDat',''))
    c = c.replace('@time@',statik.get('time',''))
    c = c.replace('@modeDat@',statik.get('modeDat',''))

    return [a,b,c]


def disca(ligua):
    final = open('descrimmc/'+ligua+'/analiDisca.descri').read()
    return final
