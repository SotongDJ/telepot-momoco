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
#def main(usrid,tank,lim,keytim,cond,targe):
def main(usrid,setto):
    keytim,conda,conde,targe,karen,plim,pleng = setto.split(' ')
    lim=int(plim)
    leng=int(pleng)
    libra = mmcdb.opendb(usrid)
    timon = timo(keytim,libra)
    gas = {}
    gos = {}
    gis = {}
    gus = {}
    som = 0
    uuid = []
    for tim in timon:
        for uid in libra['key']['datte'][tim]:
            if libra['raw'][uid]['karen'] == karen:
                if libra['raw'][uid][conda] == conde:
                    tat=libra['raw'][uid]['datte']+'　'+libra['raw'][uid]['fromm']+'　'+karen+' '+libra['raw'][uid]['price']
                    tat=tat+'\n　　　　　'+libra['raw'][uid]['klass']+'　'+libra['raw'][uid]['namma']+'　'+libra['raw'][uid]['shoop']
                    uuid.append(tat)
                    try:
                        gas[libra['raw'][uid][targe]] = gas[libra['raw'][uid][targe]] + int(libra['raw'][uid]['price'])
                    except KeyError:
                        gas[libra['raw'][uid][targe]] = int(libra['raw'][uid]['price'])
    som = sum(list(gas.values()))
    for nana in list(gas):
        lata = round((gas[nana]/som)*(lim*lim))
        pprint.pprint([lata,'=gas[',nana,']',gas[nana],'/',som,')*(',lim*lim,')'])
        gos[nana]=lata
        loto = round((gas[nana]/som)*(100),2)
        gus[nana]=loto
        try:
            gis[gas[nana]].append(nana)
        except KeyError:
            gis[gas[nana]]=[nana]
    nanga = sorted( gis , reverse = True)
    #tank = 'abcdefigmhnjrkspuqvtwyxz'
    pri = []
    #pro = 0
    pprint.pprint([nanga,gis])
    for nume in nanga:
        for itei in gis[nume]:
            nota = gos[itei]
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
                    #pri[-1]=pri[-1]+tank[pro]*(lim-rok)
                    pri[-1]=pri[-1]+miro*(lim-rok)
                    #print(pri[-1])
                    nota = nota + rok - lim
                if nota > lim:
                    tik = int(nota/lim)
                    tok = nota % lim
                    for n in range(0,tik):
                #        print(tank[pro]*10)
                #        pri.append(tank[pro]*lim)
                        pri.append(miro*lim)
                #    pri.append(tank[pro]*tok)
                    pri.append(miro*tok)
                    #pro=pro+1
                    pprint.pprint([itei,nota,rok,lim])
                elif nota <= lim:
                #    pri.append(tank[pro]*nume)miro
                    pri.append(miro*nota)
                    #pro=pro+1
                    pprint.pprint([itei,nota,rok,lim])
            elif nota + rok <= lim:
                #pri[-1]=pri[-1]+tank[pro]*nume
                pri[-1]=pri[-1]+miro*nota
                #print(pri[-1])
                #pro=pro+1
                pprint.pprint([itei,nota,rok,lim])
    des=""
    for m in nanga:
        for n in gis[m]:
            nana = n
            des=des+'　'+nana[0]+'　'+nana+'\n　　　'+karen+' '+str(gas[nana])+' ('+str(gus[nana])+'%, '+str(gos[nana])+')\n'
    final = [
        'Analytics Card',
        'Record:\n——————————\n  '+'\n  '.join(uuid)+'\n',
        'Graph of Ratio:\n——————————\n'+'\n'.join(pri)+'\n',
        'Description:\n——————————\n'+des+"\n　Total: "+str(karen)+'　'+str(som)+' ('+str(round(sum(list(gus.values())),2))+'%, '+str(sum(list(gos.values())))+')']
    return [final[0]]+final[leng:4]
