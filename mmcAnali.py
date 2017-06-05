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
        desta.append(diasa+'　'+m)
        desta.append(('　'*(nugra+1)+pttl))
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

def aKaun(usrid,dicto):
    libra = mmcdb.opendb(usrid)
    rawdb = libra.get('raw',{})
    keydb = libra.get('key',{})

    karatio = mmcdb.openKaratio()
    saita = mmcdb.openSetting(usrid)
    karen = saita.get('karen','')

    dtempo = dicto.get('dtempo')
    utempo = dicto.get('utempo')
    timon = tima(dtempo,utempo,libra)

    targe = dicto.get('targe','')
    cokas = dicto.get('cokas','')
    balan = dicto.get('balan','0')

    idsrc = [] # uuid set (related with cokas)
    tiset = [] # uuid set (related with tempo)
    ssalk = mmcDefauV.keywo('ssalk')
    rslib = {} # rs = result
    lelib = {'nummo':0, 'toooo':0, 'fromm':0, 'datte':0, cokas:0}
    uilib = {} # ui = uuid sublib
    dtlib = {} # dt = datte sublib
    colib = {} # co = co
    inval = 0.0
    outva = 0.0

    for tiora in timon:
        tiset.extend(keydb.get('datte',{}).get(tiora,[]))

    if targe in keydb.get('fromm',{}).keys():
        print(targe + ' in fromm')
        idsrc.extend(keydb.get('fromm',{}).get(targe,[]))

    if targe in keydb.get('toooo',{}).keys():
        print(targe + ' in toooo')
        idsrc.extend(keydb.get('toooo',{}).get(targe,[]))

    idset = sorted(list( set(idsrc) - ( set(idsrc)-set(tiset) )))
    # uuid set ( final )
    nummo = 0

    for uuid in idset:
        idlib = rawdb.get(uuid,{})
        fromm = ''
        toooo = ''
        nummo = nummo + 1

        if idlib.get('fromm','') == targe :

            if idlib.get('karen','') == karen:
                price = round(float(idlib.get('price','')),2)
            else:
                kaset = idlib.get('karen','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('price','')) * rate),2)

            fromm = tool.roundostr(price)
            outva = outva + price

        elif idlib.get('toooo','') == targe :

            if idlib.get('tkare','') == karen:
                price = round(float(idlib.get('tpric','')),2)
            else:
                kaset = idlib.get('tkare','')+karen
                rate = float(karatio[kaset])
                price = round((float(idlib.get('tpric','')) * rate),2)

            toooo = tool.roundostr(price)
            inval = inval + price

        unino = tool.uni(str(nummo))

        mdlib = uilib.get(uuid,{})
        mdlib.update({
            'nummo' : str(nummo),
            'unino' : unino,
            'fromm' : fromm,
            'toooo' : toooo,
        })
        uilib.update({ uuid : mdlib })

        if len(unino) > lelib.get('nummo',0):
            lelib.update({ 'nummo' : len(unino) })

        for keyo in ['fromm','toooo']:
            if mdlib.get(keyo,'') != '':
                lalal = mdlib.get(keyo,'')
                lelel = len(tool.roundostr(lalal))
                if lelel > lelib.get(keyo,0):
                    lelib.update({ keyo : lelel })

        datte = tool.uni(idlib.get('datte','          ').replace('-0','- ')[5:10])
        mdlis = dtlib.get(datte,[])
        mdlis.append( str(nummo) )
        dtlib.update({ datte : mdlis })
        if len(datte) > lelib.get('datte',0):
            lelib.update({ 'datte' : len(datte) })

        cokey = idlib.get(cokas,'')
        mdlis = colib.get(cokey,[])
        mdlis.append( str(nummo) )
        colib.update({ cokey : mdlis })
        if len(cokey) > lelib.get(cokas,0):
            lelib.update({ cokas : len(cokey) })

    rslib.update({ 'uilib' : uilib })
    rslib.update({ 'colib' : colib })
    rslib.update({ 'dtlib' : dtlib })
    rslib.update({ 'lelib' : lelib })

    oriva = float(balan) - inval + outva
    rslib.update({ 'calcu' : {
        'insum' : tool.roundostr(inval),
        'otsum' : tool.roundostr(outva),
        'oriva' : tool.roundostr(oriva),
        'balva' : tool.roundostr(balan),
        } })

#    pprint.pprint(rslib,width=200,compact=True)

    codes = ''
    for cokey in colib.keys():
        codes = codes + cokey+':\n'
        conte = "　"
        conut = 0
        for iteme in colib.get(cokey):
            if conut + len(iteme+'，') >= 13:
                conte = conte + '\n　' + iteme + '，'
                conut = len(iteme+'，')
            else:
                conte = conte + iteme + '，'
                conut = conut + len(iteme+'，')
        codes = codes + conte + '\n\n'

    dtdes = ''
    for dtkey in dtlib.keys():
        dtdes = dtdes + dtkey +':\n'
        conte = "　"
        conut = 0
        for iteme in dtlib.get(dtkey):
            if conut + len(iteme+'，') >= 13:
                conte = conte + '\n　' + iteme + '，'
                conut = len(iteme+'，')
            else:
                conte = conte + iteme + '，'
                conut = conut + len(iteme+'，')
        dtdes = dtdes + conte + '\n\n'

    uides = ''

    for uuid in sorted(list(uilib.keys())):
        unino = uilib.get(uuid).get('nummo')
        if len(unino) < lelib.get('nummo',0):
            unino = '　'*(lelib.get('nummo',0) - len(unino)) + unino

        toooo = uilib.get(uuid).get('toooo')
        if len(toooo) < lelib.get('toooo',0):
            toooo = '　'*(lelib.get('toooo',0) - len(toooo)) + toooo

        fromm = uilib.get(uuid).get('fromm')
        if len(fromm) < lelib.get('fromm',0):
            fromm = '　'*(lelib.get('fromm',0) - len(fromm)) + fromm

        uides = uides + tool.uni(unino + ' ' + toooo + ' ' + fromm + '\n')

    rslib.update({ 'codes' : codes })
    rslib.update({ 'dtdes' : dtdes })
    rslib.update({ 'uides' : uides })

    return rslib

def listClass(keywo):
    finno = ""
    skdic = mmcDefauV.keywo('ssalk')
    listo = list(mmcDefauV.keywo('temra'))
    for intta in listo:
        finno = finno +'>'+skdic.get(intta)+'\n　/set_'+keywo+'_as_'+intta+'\n'
    return finno
