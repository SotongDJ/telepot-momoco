import json, pprint
import tool, auth

def apmod(mode,text):
    mode.append(text)
    return mode

def ckmod(mode):
    modo = mode[-1]
    return modo

def popmod(mode):
    try:
        mode.pop()
        return mode
    except IndexError:
        print("IndexError: pop from empty list")
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
    filla = open(tool.path('log/mmcbot',usrid)+tool.date(5,'-'),'a')
    #print("--- pra "+text+"---")
    filla.write(text+" = "+pprint.pformat(thing)+"""
""")
    filla.close()

def cmdzDate(setta):
    pri = ''
    for n in setta:
        m = n.replace('-','_')
        pri = pri + '  /ch_'+m+'  '+n+'\n\n'
    return pri

def filteDate(setta,leve):
    if leve == 'day':
        return set(setta)
    elif leve == 'month':
        conta = []
        for n in setta:
            conta.append(n[0:7])
        return set(conta)
    elif leve == 'year':
        conta = []
        for n in setta:
            conta.append(n[0:4])
        return set(conta)
