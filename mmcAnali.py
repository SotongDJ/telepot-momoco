import mmcdb, pprint
import halfu
from libmsg import listMsg
# print(trial3.main(chat_id,20,'2017-04',['shoop',?],'namma'),'TWD')
# print(trial3.main(chat_id,20,'2017-04',['klass',?],'shoop','TWD'))
# print(trial3.main(chat_id,'2017-04 klass  shoop  15'))
def timo(keywo,lib):
    timo=[]
    for n in lib['key']['datte']:
        if keywo in n:
            timo.append(n)
    timo.sort()
    return timo

def main(usrid,keytim,conda,conde,targe,karen,lim,leng):
    libra = mmcdb.opendb(usrid)
    timon = timo(keytim,libra)
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

    print('ges : '+pprint.pformat(ges))
    print('gese : '+pprint.pformat(gese))
    print('gas : '+pprint.pformat(gas))
    print('gisi : '+pprint.pformat(gisi))

    som = sum(list(gas.values()))
    print(' som : '+pprint.pformat(som))

    for nana in list(gas):
        print('nana : '+pprint.pformat(nana))

        lata = round((gas[nana]/som)*(lim*lim))
        gos.update( { nana : lata } )
        print(' lata : '+pprint.pformat(lata))

        loto = round((gas[nana]/som)*(100),2)
        gus.update( { nana : loto } )
        print(' loto : '+pprint.pformat(loto))

        laf = gis.get(gas[nana],[])
        laf.append(nana)
        gis.update( { gas[nana] : laf } )


    print('gos : '+pprint.pformat(gos))
    print('gus : '+pprint.pformat(gus))
    print('gis : '+pprint.pformat(gis))
    nanga = sorted( gis , reverse = True)
    print('nanga : '+pprint.pformat(nanga))

    statik = []
    laf = sorted(gisi)
    statik.append('Max : '+pprint.pformat( set( gisi.get( laf[-1],'' ) ) ).replace('{','').replace('}','')+' (Price: '+str(laf[-1])+')')
    statik.append('Min : '+pprint.pformat( set( gisi.get( laf[0],'' ) ) ).replace('{','').replace('}','')+' (Price: '+str(laf[0])+')')
    lof = sorted(gese)
    lef = []
    luf = []
    for daf in gese.get(lof[-1],''):
        lef.append(gas.get( daf,'' ))
        luf.extend(ges.get( daf,[]) )
    statik.append('Mode : '+pprint.pformat( gese.get(lof[-1],'') ).replace('[','').replace(']',''))
    statik.append('　　Times: '+str(lof[-1]))
    statik.append('　　Each: '+pprint.pformat(luf).replace('[','').replace(']',''))
    statik.append('　　Total: '+pprint.pformat(lef).replace('[','').replace(']',''))

    pri = []
    for nume in nanga:
        print('nume : '+pprint.pformat(nume))
        for itei in gis[nume]:
            print('itei : '+pprint.pformat(itei))
            nota = gos[itei]
            print('nota : '+pprint.pformat(nota))
            try:
                itei[0].encode('latin-1')
                miro=halfu.fullen(itei[0])
            except UnicodeEncodeError:
                miro=itei[0]
            try:
                rok = len(pri[-1])
            except IndexError:
                pri = ['']
                rok = 0
            pprint.pprint([itei,nota,rok,lim])
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
                    pprint.pprint([itei,nota,rok,lim])
                elif nota <= lim:
                    pri.append(miro*nota)
                    pprint.pprint([itei,nota,rok,lim])
            elif nota + rok <= lim:
                pri[-1]=pri[-1]+miro*nota
                print('[itei,nota,rok,lim]')
                pprint.pprint([itei,nota,rok,lim])

    des=""
    for m in nanga:
        for n in gis[m]:
            nana = n
            des=des+'　'+nana[0]+'　'+nana+'\n　　　'+karen+' '+str(gas[nana])+' ('+str(gus[nana])+'%, '+str(gos[nana])+')\n'
    final = [
        'Analytics Cards',
        'Graph of Ratio:\n——————————\n'+'\n'.join(pri)+'\n',
        'Description:\n——————————\n'+des+"\n　Total: "+str(karen)+'　'+str(som)+' ('+str(round(sum(list(gus.values())),2))+'%, '+str(sum(list(gos.values())))+')',
        'Statistics:\n——————————\n  '+'\n  '.join(statik)+'\n',]
    return [final[0]]+final[leng:4]
