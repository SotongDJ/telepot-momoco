import pprint, np
import mmcdb, tool, mmcDefauV

def tima(downlimit,uplimit,lib):
    tok = []
    tik = sorted(set(lib['key']['datte'].keys()))
    print('tik : '+pprint.pformat(tik,compact=True))
    toka = 0
    toko = len(tik)
    try:
        toka = tik.index(downlimit)
    except ValueError:
        ck = 0
        for n in sorted(tik, reverse=True):
            if downlimit[0:8] in n:
                toka = tik.index(n)
                ck = 1
                #print('toka got : primary')
        if ck == 0:
            for n in sorted(tik, reverse=True):
                if downlimit[0:4] in n:
                    toka = tik.index(n)
                    ck = 1
                    #print('toka got : secokasry')
    try:
        toko = tik.index(uplimit)
    except ValueError:
        ck = 0
        for n in tik:
            if uplimit[0:8] in n:
                toko = tik.index(n)
                ck = 1
                #print('toko got : primary')
        if ck == 0:
            for n in tik:
                if uplimit[0:4] in n:
                    toko = tik.index(n)
                    ck = 1
                    #print('toko got : secokasry')
    tok = tik[toka:toko+1]
    print('tok : '+pprint.pformat(tok,compact=True))
    return tok

def abratio(usrid,dicto):
    saita = mmcdb.openSetting(usrid)
    karen = saita['karen']
    lim = saita['screen']

    dtempo=dicto.get('dtempo')
    utempo=dicto.get('utempo')
    targe=dicto.get('targe')
    cokas=dicto.get('cokas')
    cokey=dicto.get('cokey')

    karatio = mmcdb.openKaratio()

    libra = mmcdb.opendb(usrid)
    timon = tima(dtempo,utempo,libra)
    gas = {} # { targe : price'int'total}
    gos = {} # { targe : (price'int'total/sum)*(lim^2) }
    gis = {} # { price'int'total : [targe1,targe2...] }
    gisi = {} # { price'int'indi : [targe1,targe2...] }
    gus = {} # { targe : (price'int'total/sum)*100 }
    ges = {} # { targe : [price1'str'indi,price2'str'indi...] }
    gese = {} # { len([price1'str'indi,price2'str'indi...])'int': [targe1, targe2] }
    som = 0
    rawdb = libra['raw']
    keydb = libra['key']
    kdatedb = keydb.get('datte',{})
    for tim in timon:
        for uid in kdatedb.get(tim,[]):
            if libra['raw'][uid][cokas] == cokey:
                if libra['raw'][uid]['karen'] == karen:
                    price = round(float(libra['raw'][uid]['price']),2)
                else:
                    rate = float(karatio[libra['raw'][uid]['karen']+karen])
                    price = round(float(libra['raw'][uid]['price']) * rate,2)
                laf = ges.get(libra['raw'][uid][targe],[])
                laf.append(str(price))
                ges.update( { libra['raw'][uid][targe] : laf } )

                lif = gese.get(len(laf),[])
                lif.append(libra['raw'][uid][targe])
                gese.update( { len(laf) : lif } )

                lof = gas.get(libra['raw'][uid][targe],0.00)
                lof = round(lof + price,2)
                gas.update( { libra['raw'][uid][targe] : lof } )

                lef = gisi.get(price,[])
                lef.append(libra['raw'][uid][targe])
                gisi.update( { price : lef } )

    print('ges : '+pprint.pformat(ges,compact=True))
    print('gese : '+pprint.pformat(gese,compact=True))
    print('gas : '+pprint.pformat(gas,compact=True))
    print('gisi : '+pprint.pformat(gisi,compact=True))

    som = round(sum(list(gas.values())),2)
    if round(som,2) == 0.00:
        return {'pri':['No Data','Maybe using wrong combination']}
    sam = str(som)
    print(' som : '+pprint.pformat(som))

    for nana in list(gas):
        #print('nana : '+pprint.pformat(nana))

        lata = round((gas[nana]/som)*(lim*lim))
        gos.update( { nana : lata } )
        #print(' lata : '+pprint.pformat(lata))

        loto = round((gas[nana]/som)*(100),2)
        gus.update( { nana : loto } )
        #print(' loto : '+pprint.pformat(loto))

        laf = gis.get(gas[nana],[])
        laf.append(nana)
        gis.update( { gas[nana] : laf } )


    print('gos : '+pprint.pformat(gos,compact=True))
    print('gus : '+pprint.pformat(gus,compact=True))
    print('gis : '+pprint.pformat(gis,compact=True))
    par = str(round(sum(list(gus.values())),2))
    kub = str(sum(list(gos.values())))

    nanga = sorted( gis , reverse = True)
    print('nanga : '+pprint.pformat(nanga,compact=True))

    statik = {}
    laf = sorted(gisi)
    statik.update({ 'max' : pprint.pformat( set( gisi.get( laf[-1],'' ) ) ).replace('{','').replace('}','') })
    statik.update({ 'maxPc' : str(laf[-1]) })
    statik.update({ 'min' : pprint.pformat( set( gisi.get( laf[0],'' ) ) ).replace('{','').replace('}','') })
    statik.update({ 'minPc' : str(laf[0]) })

    lof = sorted(gese)
    dafro = ''
    for daf in gese.get(lof[-1],''):
        dafro = dafro + '－'+daf+' '+karen+' '+pprint.pformat(gas.get(daf),compact=True).replace('[','').replace(']','')+'\n'
        dafro = dafro + '　'+pprint.pformat(ges.get(daf),compact=True).replace('[','( ').replace(']',' )')+'\n'
    statik.update({ 'time' : str(lof[-1]) })
    statik.update({ 'dafro' : dafro })

    pri = []
    for nume in nanga:
        print('nume : '+pprint.pformat(nume))
        for itei in gis[nume]:
            #print('itei : '+pprint.pformat(itei))
            nota = gos[itei]
            #print('nota : '+pprint.pformat(nota))
            miro = tool.uni(itei[0])
            try:
                rok = len(pri[-1])
            except IndexError:
                pri = ['']
                rok = 0
            pprint.pprint([itei,nota,rok,lim],compact=True)
            if nota + rok >lim:
                if rok < lim:
                    pri[-1]=pri[-1]+miro*(lim-rok)
                    nota = nota + rok - lim
                if nota > lim:
                    tik = int(nota/lim)
                    tok = nota % lim
                    for n in range(0,tik):
                        pri.append(miro*lim)
                    pri.append(miro*tok)
                    pprint.pprint([itei,nota,rok,lim],compact=True)
                elif nota <= lim:
                    pri.append(miro*nota)
                    pprint.pprint([itei,nota,rok,lim],compact=True)
            elif nota + rok <= lim:
                pri[-1]=pri[-1]+miro*nota
                print('[itei,nota,rok,lim]')
                pprint.pprint([itei,nota,rok,lim],compact=True)

    des=""
    for m in nanga:
        for n in gis[m]:
            nana = n
            des=des+nana[0]+'　'+nana+'\n　　'+karen+' '+str(gas[nana])+' ('+str(gus[nana])+'%, '+str(gos[nana])+')\n'
    resut={}

    resut.update({'dtempo': dtempo })
    resut.update({'utempo': utempo })
    resut.update({'cokas': cokas })
    resut.update({'cokey': cokey })
    resut.update({'targe': targe })
    resut.update({'pri': pri })
    resut.update({'des': des })
    resut.update({'karen': karen })
    resut.update({'sam': sam })
    resut.update({'par': par })
    resut.update({'kub': kub })
    resut.update({'statik': statik })

    return resut

def atren(usrid,dicto):
    dtempo=dicto.get('dtempo')
    utempo=dicto.get('utempo')
    leve=dicto.get('leve')
    cokas=dicto.get('cokas')
    cokey=dicto.get('cokey')
    karatio = mmcdb.openKaratio()

    saita = mmcdb.openSetting(usrid)
    karen = saita['karen']
    lim = saita['screen'] -3

    libra = mmcdb.opendb(usrid)
    timon = tima(dtempo,utempo,libra)
    meksi = 0.00
    rawdb = libra['raw']
    keydb = libra['key']
    kdatedb = keydb.get('datte',{})
    miro = tool.uni(cokey[0])
    gas = {} # { datte : price'int'sum}
    gaf = {} # { price'int'sum : [datte]}
    gasa = {} # { datte : [price'int'indi]}
    gafa = {} # { price'int'indi : [datte] }
    gaga = {} # { len([price'int'indi]) : [datte] }
    ges = {} # { datte : (price'int'sum)/meksi*lim}
    gus = {} # { num : datte}

    for tim in timon:
        for uid in kdatedb.get(tim,[]):
            datte = rawdb[uid]['datte'][0:leve]
            if rawdb[uid][cokas] == cokey:
                if libra['raw'][uid]['karen'] == karen:
                    price = round(float(libra['raw'][uid]['price']),2)
                else:
                    rate = float(karatio[libra['raw'][uid]['karen']+karen])
                    price = round(float(libra['raw'][uid]['price']) * rate,2)
                laf = gas.get(datte,0)
                laf = round(laf + price,2)
                gas.update( { datte : laf } )

                lafa = gasa.get(datte,[])
                lafa.append(str(price))
                gasa.update( { datte : lafa } )

                lafo = gafa.get(price,[])
                lafo.append(datte)
                gafa.update( { price : lafo } )

                if laf > meksi:
                    meksi = laf
            else:
                laf = gas.get(datte,0)
                gas.update( { datte : laf } )

                lafa = gasa.get(datte,[])
                gasa.update( { datte : lafa } )

    print('gas : '+pprint.pformat(gas,compact=True))
    print('gasa : '+pprint.pformat(gasa,compact=True))
    print('gafa : '+pprint.pformat(gafa,compact=True))
    dias = sorted(gas)
    print('dias : '+pprint.pformat(dias,compact=True))
    if round(meksi,2) == 0.00:
        return {'graf':['No Data','Maybe using wrong combination']}
    meksi = round(meksi,2)
    print('meksi : '+pprint.pformat(meksi))
    nume = 1
    for dat in dias:
        daf = round((gas.get(dat,0) / meksi) * lim)
        ges.update( { dat : daf } )
        gus.update( { nume : dat } )
        nume = nume + 1

    print('ges : '+pprint.pformat(ges,compact=True))
    print('gus : '+pprint.pformat(gus,compact=True))

    # x against y
    nugra = len(tool.uni(str(sorted(gus)[-1])))
    print('nugra : '+pprint.pformat(nugra))

    graf = []
    for n in sorted(gus):
        m = gus.get(n)
        laf = ges.get(m,0)
        diasa = tool.uni(str(n))
        if len(diasa) < nugra:
            diasa = ('　' * (nugra-len(diasa))) + diasa
        lina = diasa + '｜' + (miro * laf)# + ' ' + str(gas.get(m))
        graf.append(lina)

    desta=[]
    for n in sorted(gus):
        diasa = tool.uni(str(n))
        if len(diasa) < nugra:
            diasa = ('　' * (nugra-len(diasa))) + diasa
        m = gus.get(n)
        pttl = karen+' '+str(round(gas.get(m),2))
        ofe = pprint.pformat(gasa.get(m))#.replace('[','').replace(']','').replace('\'','')
        desta.append(diasa+'：')
        desta.append('　'*(nugra-1) + m )
        desta.append('　'*(nugra-1) + pttl + '\n' )
        #desta.append('　'+ofe)
    des='\n'.join(desta)

    oridat = [x for x in list(gas.values())]
    sam = round(sum(oridat),2)
    vam = round(sam/len(oridat),2)
    fildat = [x for x in list(gas.values()) if abs(x - np.mean(oridat)) <= (np.std(oridat)*1)]
    san = round(sum(fildat),2)
    van = round(san/len(fildat),2)

    statik = {}
    for m in gas.keys():
        n = gas.get(m)
        laf = gaf.get(n,[])
        laf.append(m)
        gaf.update( { n : laf } )
    print('gaf : '+pprint.pformat(gaf, compact=True))
    for m in gasa.keys():
        n = len(gasa.get(m))
        laf = gaga.get(n,[])
        laf.append(m)
        gaga.update( { n : laf } )
    print('gaga : '+pprint.pformat(gaga, compact=True))

    laf = sorted(gafa)
    statik.update({ 'sinMax' : pprint.pformat( set( gafa.get( laf[-1],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','') })
    statik.update({ 'sinMaxPc' : str(laf[-1]) })
    statik.update({ 'sinMin' : pprint.pformat( set( gafa.get( laf[0],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','') })
    statik.update({ 'sinMinPc' : str(laf[0]) })

    laf = sorted(gaf)
    oveMaxDat=''
    for daf in gaf.get( laf[-1],[''] ):
        oveMaxDat = oveMaxDat+'－'+daf+' '+pprint.pformat(gasa.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'oveMaxPc' : str(laf[-1]) })
    statik.update({ 'oveMaxDat' : oveMaxDat })

    oveMinDat=''
    if laf[0] != 0:
        mino = laf[0]
    else:
        try:
            mino = laf[1]
        except KeyError:
            mino = laf[0]
    for daf in gaf.get( mino,[''] ):
        oveMinDat = oveMinDat+'－'+daf+' '+pprint.pformat(gasa.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'oveMinPc' : str(mino) })
    statik.update({ 'oveMinDat' : oveMinDat })

    laf = sorted(gaga)
    modeDat=''
    for daf in gaga.get(laf[-1],''):
        modeDat = modeDat+'－'+daf+' '+karen+' '+pprint.pformat(gas.get(daf),compact=True).replace('[','').replace(']','')+'\n'
        modeDat = modeDat+'　'+pprint.pformat(gasa.get(daf),compact=True).replace('[','（').replace(']','）')+'\n'
    statik.update({ 'time' : str(laf[-1]) })
    statik.update({ 'modeDat' : modeDat })

    resut={}

    resut.update({'dtempo': dtempo })
    resut.update({'utempo': utempo })
    resut.update({'cokas': cokas })
    resut.update({'cokey': cokey })
    resut.update({'graf': graf })
    resut.update({'des': des })
    resut.update({'karen': karen })
    resut.update({'sam': sam })
    resut.update({'vam': vam })
    resut.update({'san': san })
    resut.update({'van': van })
    resut.update({'statik': statik })

    return resut

def akaun(usrid,dicto):
    libra = mmcdb.opendb(usrid)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})
    rslib = {} # rs = result

    karatio = mmcdb.openKaratio()
    saita = mmcdb.openSetting(usrid)
    karen = saita.get('karen','')

    dtempo = dicto.get('dtempo')
    utempo = dicto.get('utempo')
    rslib.update({ 'dtempo' : dtempo })
    rslib.update({ 'utempo' : utempo })
    timon = tima(dtempo,utempo,libra)

    acuno = dicto.get('acuno','')
    rslib.update({ 'acuno' : acuno })
    cokas = dicto.get('cokas','')
    rslib.update({ 'cokas' : cokas })
    balan = float(dicto.get('balan','0.0'))

    idsrc = [] # uuid set (related with cokas)
    tiset = [] # uuid set (related with tempo)
    coset = [] # cokey set
    transle = mmcDefauV.keywo('transle')

    for tiora in timon:
        tiset.extend(keydb.get('datte',{}).get(tiora,[]))

    if acuno in keydb.get('fromm',{}).keys():
        print(acuno + ' in fromm')
        idsrc.extend(keydb.get('fromm',{}).get(acuno,[]))

    if acuno in keydb.get('toooo',{}).keys():
        print(acuno + ' in toooo')
        idsrc.extend(keydb.get('toooo',{}).get(acuno,[]))

    idset = sorted(list( set(idsrc) - ( set(idsrc)-set(tiset) )))
    # uuid set ( final )

    uilib = {} # ui = uuid
    colib = {} # co = cokey
    folib = {} # fo = fromm
    tolib = {} # to = toooo
    inval = 0.0
    outva = 0.0

    for uuid in idset:
        idlib = rawdb.get(uuid,{})
        fromm = ''
        toooo = ''

        if idlib.get('fromm','') == acuno :

            if idlib.get('karen','') == karen:
                price = round(float(idlib.get('price','')),2)
            else:
                kaset = idlib.get('karen','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('price','')) * rate),2)

            fromm = tool.roundostr(price)
            outva = outva + price

        elif idlib.get('toooo','') == acuno :

            if idlib.get('tkare','') == karen:
                price = round(float(idlib.get('tpric','')),2)
            else:
                kaset = idlib.get('tkare','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('tpric','')) * rate),2)

            toooo = tool.roundostr(price)
            inval = inval + price

        cokey = idlib.get(cokas,'')

        if cokey not in coset:
            uilib.update({ uuid : cokey })
            coset.append(cokey)

        mdlis = colib.get(cokey,[])
        mdlis.append(uuid)
        colib.update({ cokey : mdlis })

        mdlis = folib.get(cokey,[])
        mdlis.append(fromm)
        folib.update({ cokey : mdlis })

        mdlis = tolib.get(cokey,[])
        mdlis.append(toooo)
        tolib.update({ cokey : mdlis })

    pebal = balan - inval + outva
    pesum = tool.roundostr(pebal)
    otsum = tool.roundostr(outva)
    insum = tool.roundostr(inval)
    basum = tool.roundostr(balan)
    rslib.update({ 'otsum' : otsum })
    rslib.update({ 'insum' : insum })
    rslib.update({ 'basum' : basum })

    rslib.update({ 'uilib' : uilib })
    rslib.update({ 'colib' : colib })
    rslib.update({ 'folib' : folib })
    rslib.update({ 'tolib' : tolib })

    nummo = 0
    pilib = {} # pi = price
    lelib = {'nummo':0, 'tosum':0, 'fosum':0, 'cokey':0}

    for uuid in uilib.keys():
        nummo = nummo + 1
        cokey = uilib.get(uuid,'')

        foset = [float(x) for x in folib.get(cokey) if x != '']
        if sum(foset) != 0.0:
            fosum = tool.roundostr(sum(foset))
        else:
            fosum = ''

        toset = [float(x) for x in tolib.get(cokey) if x != '']
        if sum(toset) != 0.0:
            tosum = tool.roundostr(sum(toset))
        else:
            tosum = ''

        mdlib = {
            'cokey' : cokey,
            'fosum' : fosum,
            'tosum' : tosum,
        }
        pilib.update({ nummo : mdlib })

        for keyo in mdlib.keys():
            if len(mdlib.get(keyo,'')) > lelib.get(keyo,0):
                lelib.update({ keyo : len(mdlib.get(keyo,'')) })

        for sumwo,sumke in [['tosum',insum],['fosum',otsum]]:
            if len(sumke) > lelib.get(sumwo,0):
                lelib.update({ sumwo : len(sumke) })

        lelib.update({ 'nummo' : len(str(nummo))})

    rslib.update({ 'lelib' : lelib })
    rslib.update({ 'pilib' : pilib })

    pides = '' # pi = price

    lingua = mmcdb.openSetting(usrid).get('lingua')
    transle = mmcDefauV.keywo('transle',lingua=lingua)
    namcokas = transle.get(cokas,'')

    a = '　'*lelib.get('nummo',0)
    b = round((lelib.get('tosum',0) - 2)/2)
    bb = '　'*b
    c = '　'*(lelib.get('tosum',0) - 2 - b)
    d = round((lelib.get('fosum',0) - 3)/2)
    dd = '　'*d
    e = lelib.get('fosum',0) - 3 - d

    f = a +'　'+bb+'ＩＮ'+c+'　'+dd+'ＯＵＴ'
    g = len(f)+e
    pides = f + '\n' + '—'*g + '\n'

    for nummo in sorted(list(pilib.keys())):
        fosum = pilib.get(nummo,{}).get('fosum')
        tosum = pilib.get(nummo,{}).get('tosum')

        if len(str(nummo)) < lelib.get('nummo',0):
            a = '　'*(lelib.get('nummo',0) - len(str(nummo)))
        else:
            a = ''

        if len(tosum) < lelib.get('tosum',0):
            b = '　'*(lelib.get('tosum',0) - len(tosum))
        else:
            b = ''

        if len(fosum) < lelib.get('fosum',0):
            c = '　'*(lelib.get('fosum',0) - len(fosum))
        else:
            c = ''
        d = a + str(nummo) + '　'  + b + tosum + '　'  + c + fosum
        pides = pides + tool.uni(d) + '\n'

    pides = pides + '—'*g + '\n'

    a = '　'*lelib.get('nummo',0)

    if len(insum) < lelib.get('tosum',0):
        b = '　'*(lelib.get('tosum',0) - len(insum))
    else:
        b = ''

    if len(otsum) < lelib.get('fosum',0):
        c = '　'*(lelib.get('fosum',0) - len(otsum))
    else:
        c = ''

    e = '∑' + a + '　'  + b + insum + '　'  + c + otsum
    pides = pides + tool.uni(e) + '\n'
    pides = pides + '—'*g + '\n' + f

    codes = '' # co = cokey

    for nummo in sorted(list(pilib.keys())):
        cokey = pilib.get(nummo,{}).get('cokey')

        if len(str(nummo)) < lelib.get('nummo',0):
            a = '　'*(lelib.get('nummo',0) - len(str(nummo)))
        else:
            a = ''

        d = a + str(nummo) + '：'
        codes = codes + tool.uni(d) + cokey + '\n'

    rslib.update({ 'pides' : pides })
    rslib.update({ 'codes' : codes })

    lefin = 0

    if lelib.get('fosum',0) > lelib.get('tosum',0):
        lefin = lelib.get('fosum',0)
    else:
        lefin = lelib.get('tosum',0)

    if len(basum) > lefin:
        lefin = len(basum)
    elif len(pesum) > lefin:
        lefin = len(pesum)

    blanc = '　'*lefin
    pefin = '　'*(lefin-len(pesum)) + pesum
    infin = '　'*(lefin-len(insum)) + insum
    otfin = '　'*(lefin-len(otsum)) + otsum
    linec = '—'*lefin
    bafin = '　'*(lefin-len(basum)) + basum

    rslib.update({ 'blanc' : blanc })
    rslib.update({ 'pefin' : pefin })
    rslib.update({ 'infin' : infin })
    rslib.update({ 'otfin' : otfin })
    rslib.update({ 'linec' : linec })
    rslib.update({ 'bafin' : bafin })

    return rslib

def listClass(keywo,lingua='enMY'):
    finno = ""
    skdic = mmcDefauV.keywo('transle',lingua=lingua)
    listo = sorted(list(mmcDefauV.keywo('temra')))
    for intta in listo:
        finno = finno + '/set_'+keywo+'_as_'+intta+'\n' +'＞　'+skdic.get(intta)+'\n\n'
    return finno

def check(keset):
    modda = keset.get('mode','')
    resut = False
    for keyo in mmcDefauV.keywo('staset').get(modda,[]):
        if keset.get(keyo,'') == '':
            resut = True
    return resut
