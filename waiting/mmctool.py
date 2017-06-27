import json, pprint
import tool, auth, mmcDefauV

def apmod(mode,text):
    mode.append(text)
    return mode

def ckmod(mode):
    modo = mode[-1]
    return modo

def popmod(mode):
    try:
        mode.pop()
        if len(mode) == 0:
            mode = ['']
        return mode
    except IndexError:
        print("IndexError: pop from empty list")
        mode = ['']
        return mode

def chstr(a,b,c,d): # if a == b, return c; else return d
    if a == b :
        return c
    else:
        return d

def check(file_name):
    a=open(file_name,"r")
    b=json.load(a)
    pprint.pprint(b)

def printbug(text,thing,usrid):
    filla = open(tool.path('log/mmcbot',usrid=usrid)+tool.date(modde=5),'a')
    #print("--- pra "+text+"---")
    filla.write(text+" = "+pprint.pformat(thing)+"""
""")
    filla.close()

def printvez(vez):
    veces = open(tool.path('log/mmcbot',usrid=auth.id())+tool.date(modde=1)+'.c','a')
    veces.write(str(vez))
    veces.close()
    return vez+1

def finvez(vez):
    veces = open(tool.path('log/mmcbot',usrid=auth.id())+tool.date(modde=1)+'.c','a')
    veces.write(str(vez)+"c\n")
    veces.close()
    return vez+1

def cmdzDate(setta):
    pri = ''
    for n in setta[0]:
        m = n.replace('-','_')
        pri = pri + '  /'+setta[1]+'_'+m+'  '+n+'\n\n'
    return pri

def filteDate(setta,leve):
    datte=tool.date(1,'-')
    if leve == 'day':
        conta = []
        for n in setta:
            if datte[0:7] in n:
                conta.append(n)
        return [sorted(set(conta),reverse=True),'ch']
    elif leve == 'month':
        conta = []
        for n in setta:
            if datte[0:4] in n:
                conta.append(n[0:7])
        return [sorted(set(conta),reverse=True),'Choose']
    elif leve == 'year':
        conta = []
        for n in setta:
            conta.append(n[0:4])
        return [sorted(set(conta),reverse=True),'Choose']
    elif len(leve) <= 4: # year
        conta = []
        for n in setta:
            if leve in n:
                conta.append(n[0:7])
        return [sorted(set(conta),reverse=True),'Choose']
    elif len(leve) <= 7: # month
        conta = []
        for n in setta:
            if leve in n:
                conta.append(n)
        return [sorted(set(conta),reverse=True),'ch']
    elif len(leve) <= 10: # day
        conta = []
        for n in setta:
            if leve in n:
                conta.append(n)
        return [sorted(set(conta),reverse=True),'ch']

def ul(testa,modda='',lingua='enMY'):
    resut = ''
    transle = mmcDefauV.keywo('transle',lingua=lingua)
    if testa == '':
        resut = '_____'
    else:
        if modda == 'klass' :
            resut = transle.get(testa,testa)
        else:
            resut = testa
    return resut
