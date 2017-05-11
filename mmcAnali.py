import pprint
import mmcdb, tool, mmcDefauV
#from libmsg import analiMsg

def timo(keywo,lib):
    timo=[]
    for n in lib['key']['datte']:
        if keywo in n:
            timo.append(n)
    timo.sort()
    return timo

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
                    #print('toka got : secondary')
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
                    #print('toko got : secondary')
    tok = tik[toka:toko+1]
    print('tok : '+pprint.pformat(tok,compact=True))
    return tok

def abratio(usrid,dtempo,utempo,conda,conde,targe,karen,lim):
    libra = mmcdb.opendb(usrid)
    #timon = timo(keytim,libra)
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
            if libra['raw'][uid]['karen'] == karen:
                if libra['raw'][uid][conda] == conde:
                    laf = ges.get(libra['raw'][uid][targe],[])
                    laf.append(libra['raw'][uid]['price'])
                    ges.update( { libra['raw'][uid][targe] : laf } )

                    lif = gese.get(len(laf),[])
                    lif.append(libra['raw'][uid][targe])
                    gese.update( { len(laf) : lif } )

                    lof = gas.get(libra['raw'][uid][targe],0)
                    lof = lof + int(libra['raw'][uid]['price'])
                    gas.update( { libra['raw'][uid][targe] : lof } )

                    lef = gisi.get(int(libra['raw'][uid]['price']),[])
                    lef.append(libra['raw'][uid][targe])
                    gisi.update( { int(libra['raw'][uid]['price']) : lef } )

    print('ges : '+pprint.pformat(ges,compact=True))
    print('gese : '+pprint.pformat(gese,compact=True))
    print('gas : '+pprint.pformat(gas,compact=True))
    print('gisi : '+pprint.pformat(gisi,compact=True))

    som = sum(list(gas.values()))
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
    nanga = sorted( gis , reverse = True)
    print('nanga : '+pprint.pformat(nanga,compact=True))

    statik = []
    laf = sorted(gisi)
    statik.append('Max : '+pprint.pformat( set( gisi.get( laf[-1],'' ) ) ).replace('{','').replace('}','')+' (Price: '+str(laf[-1])+')')
    statik.append('Min : '+pprint.pformat( set( gisi.get( laf[0],'' ) ) ).replace('{','').replace('}','')+' (Price: '+str(laf[0])+')')

    lof = sorted(gese)
    statik.append('Mode : ')
    statik.append('　　Times: '+str(lof[-1]))
    statik.append('　　List: ')
    for daf in gese.get(lof[-1],''):
        statik.append('　　　'+daf+' '+karen+' '+pprint.pformat(gas.get(daf),compact=True).replace('[','').replace(']',''))
        statik.append('　　　　'+pprint.pformat(ges.get(daf),compact=True).replace('[','( ').replace(']',' )'))

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
            des=des+'　'+nana[0]+'　'+nana+'\n　　　'+karen+' '+str(gas[nana])+' ('+str(gus[nana])+'%, '+str(gos[nana])+')\n'
    final = [
        'Analytics Cards\n——————————\nBetween '+dtempo+' and '+utempo+"""
    Under """+conde+' ('+mmcDefauV.keywo('ssalk')[conda]+'), \nShowing Ratio of '+mmcDefauV.keywo('ssalk')[targe],
        'Graph of Ratio:\n——————————\n'+'\n'.join(pri)+'\n',
        'Description:\n——————————\n'+des+"\n　Total: "+karen+' '+'　'+str(som)+' ('+str(round(sum(list(gus.values())),2))+'%, '+str(sum(list(gos.values())))+')',
        'Statistics:\n——————————\n　'+'\n　'.join(statik)+'\n',]
    return final

def atren(usrid,dtempo,utempo,leve,conda,conde,karen,lim):
    libra = mmcdb.opendb(usrid)
    timon = tima(dtempo,utempo,libra)
    meksi = 0
    rawdb = libra['raw']
    keydb = libra['key']
    kdatedb = keydb.get('datte',{})
    miro = tool.uni(conde[0])
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
            if rawdb[uid]['karen'] == karen:
                if rawdb[uid][conda] == conde:
                    laf = gas.get(datte,0)
                    laf = laf + int(libra['raw'][uid]['price'])
                    gas.update( { datte : laf } )

                    lafa = gasa.get(datte,[])
                    lafa.append(rawdb[uid]['price'])
                    gasa.update( { datte : lafa } )

                    lafo = gafa.get(rawdb[uid]['price'],[])
                    lafo.append(datte)
                    gafa.update( { rawdb[uid]['price'] : lafo } )

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
    #meksi = round(meksi * ((lim-1)/lim))
    print('meksi : '+pprint.pformat(meksi))
    nume = 1
    for dat in dias:
        daf = round((gas.get(dat,0) / meksi) * lim)
        ges.update( { dat : daf } )
        gus.update( { nume : dat } )
        nume = nume + 1

    print('ges : '+pprint.pformat(ges,compact=True))
    print('gus : '+pprint.pformat(gus,compact=True))

    """ # y against x
    nugra = len(tool.uni(str(meksi)))
    print('nugra : '+pprint.pformat(nugra))
    graf = []

    for m in sorted(range(1,lim+1),reverse=True):
        grada = round( (m / lim) * meksi )
        grat = tool.uni(str(grada))
        if len(grat) < nugra:
            grat = ('　' * (nugra-len(grat))) + grat
        lina = grat + '｜'
        for n in sorted(gus):
            laf = ges.get(gus.get(n,''),0)
            if laf >= m:
                lina = lina + miro
            else:
                lina = lina + '　'
            #print('(m,n:'+pprint.pformat(m)+pprint.pformat(n)+')lina : '+pprint.pformat(lina))
        graf.append(lina)
    lina = ('　' * nugra) + '＋'+ ('—' * len(gus))
    graf.append(lina)
    lina = ('　' * nugra) + '　'

    for n in sorted(gus):
        if len(str(n)) == 1:
            lina = lina + tool.uni(str(n))
        else:
            lina = lina + tool.uni(str(n)[-1])

    graf.append(lina)
    """
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

    som = 0
    desta=[]
    for n in sorted(gus):
        diasa = tool.uni(str(n))
        if len(diasa) < nugra:
            diasa = ('　' * (nugra-len(diasa))) + diasa
        m = gus.get(n)
        som = som + gas.get(m)
        pttl = karen+' '+str(gas.get(m))
        ofe = pprint.pformat(gasa.get(m))#.replace('[','').replace(']','').replace('\'','')
        desta.append(diasa+'　'+m)
        desta.append(('　'*(nugra+1)+pttl))
        #desta.append('　'+ofe)
    des='　'+'\n　'.join(desta)

    statik = []
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
    statik.append('Single: ')
    statik.append('　Max : '+pprint.pformat( set( gafa.get( laf[-1],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','')+' (Price: '+str(laf[-1])+')')
    statik.append('　Min : '+pprint.pformat( set( gafa.get( laf[0],'' ) ) ).replace('}, {',' ; ').replace('{','').replace('}','')+' (Price: '+str(laf[0])+')')

    laf = sorted(gaf)
    statik.append('Overall: ')

    statik.append('　Max : ')
    statik.append('　　Price: '+str(laf[-1]))
    statik.append('　　Date:')
    for daf in gaf.get( laf[-1],[''] ):
        statik.append('　　　'+daf+' '+pprint.pformat(gasa.get(daf),compact=True).replace('[','( ').replace(']',' )'))

    if laf[0] != 0:
        mino = laf[0]
    else:
        try:
            mino = laf[1]
        except KeyError:
            mino = laf[0]
    statik.append('　Min : ')
    statik.append('　　Price: '+str(mino))
    statik.append('　　Date:')
    for daf in gaf.get( mino,[''] ):
        statik.append('　　　'+daf+' '+pprint.pformat(gasa.get(daf),compact=True).replace('[','( ').replace(']',' )'))

    laf = sorted(gaga)
    statik.append('Mode : ')
    statik.append('　Times : '+str(laf[-1]))
    statik.append('　Date: ')
    for daf in gaga.get(laf[-1],''):
        statik.append('　　'+daf+' '+karen+' '+pprint.pformat(gas.get(daf),compact=True).replace('[','').replace(']',''))
        statik.append('　　　'+pprint.pformat(gasa.get(daf),compact=True).replace('[','( ').replace(']',' )'))

    final = [
        'Analytics Cards\n——————————\nBetween '+dtempo+' and '+utempo+"""
Showing Trend of """+conde+' ('+mmcDefauV.keywo('ssalk')[conda]+')',
        'Graph of Trend:\n——————————\n'+'\n'.join(graf),
        'Description:\n——————————\n'+des+"\n　Total: "+karen+'　'+str(som),
        'Statistics:\n——————————\n'+'\n'.join(statik)+'\n',]
    return final
