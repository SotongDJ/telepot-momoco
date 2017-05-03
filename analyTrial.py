import mmcdb, pprint
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
    keytim,conda,conde,targe,karen,plim = setto.split(' ')
    lim=int(plim)
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
                    tat=libra['raw'][uid]['datte']+'  '+libra['raw'][uid]['namma']+'  '+libra['raw'][uid]['shoop']+'\n        '
                    tat=tat+'  '+libra['raw'][uid]['klass']+'  '+libra['raw'][uid]['fromm']+'  '+karen+'  '+libra['raw'][uid]['price']
                    uuid.append(tat)
                    try:
                        gas[libra['raw'][uid][targe]] = gas[libra['raw'][uid][targe]] + int(libra['raw'][uid]['price'])
                    except KeyError:
                        gas[libra['raw'][uid][targe]] = int(libra['raw'][uid]['price'])
    som = sum(list(gas.values()))
    for nana in list(gas):
        lata = round((gas[nana]/som)*(lim*lim))
        gos[nana]=lata
        loto = str(round((gas[nana]/som)*(100),2))
        gus[nana]=loto
        try:
            gis[lata].append(nana)
        except KeyError:
            gis[lata]=[nana]
    nanga = sorted( gis , reverse = True)
    #tank = 'abcdefigmhnjrkspuqvtwyxz'
    pri = []
    #pro = 0
    for nume in nanga:
        for itei in gis[nume]:
            try:
                rok = len(pri[-1])
            except IndexError:
                pri = ['']
                rok = 0
            if nume + rok >lim:
                if rok < lim:
                    #pri[-1]=pri[-1]+tank[pro]*(lim-rok)
                    pri[-1]=pri[-1]+itei[0]*(lim-rok)
                    #print(pri[-1])
                    nume = nume + rok - lim
                    if nume > lim:
                        tik = int(nume/lim)
                        tok = nume % lim
                        for n in range(0,tik):
                    #        print(tank[pro]*10)
                    #        pri.append(tank[pro]*lim)
                            pri.append(itei[0]*lim)
                    #    pri.append(tank[pro]*tok)
                        pri.append(itei[0]*tok)
                        #pro=pro+1
                    elif nume <= lim:
                    #    pri.append(tank[pro]*nume)itei[0]
                        pri.append(itei[0]*nume)
                        #pro=pro+1
            elif nume + rok <= lim:
                #pri[-1]=pri[-1]+tank[pro]*nume
                pri[-1]=pri[-1]+itei[0]*nume
                #print(pri[-1])
                #pro=pro+1
    des=""
    for nana in list(gas):
        des=des+'  '+nana[0]+'  '+nana+'\n          '+karen+' '+str(gas[nana])+' ('+gus[nana]+'%)\n'
    final = """Analytics Card
——————————
Record:
  """+'\n  '.join(uuid)+"""

——————————
"""+'\n'.join(pri)+"""

——————————
Description:
"""+des
    return final
