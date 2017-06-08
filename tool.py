import os, time, random, subprocess, pprint, json
import halfu
def date(modde=10,text='-:'):
    a,b,c,d,e,f,g,h,i = time.localtime(time.time())
    j=[]
    for n in [a,b,c,d,e,f]:
        j.append(str(n))
    for n in range(1,6):
        if len(j[n]) == 1 :
            j[n]="0"+j[n]
    if modde == 0 : # output: ["yyyy","mm","dd","hh","mm","ss"]
        return j
    elif modde == 1 : # output: "yyyy-mm-dd" if text = '-'
        return text[0].join(j[0:3])
    elif modde == 2 : # output: "yyyy-mm-dd hh:mm:ss" if text = '-:'
        return text[0].join(j[0:2])+" "+text[1].join(j[3:6])
    elif modde == 3 : # output: "yyyymmddhhmmss"
        return "".join(j)
    elif modde == 4 : # output: "yyyymmddhhmmssrrrrrrrr" rrrr is eight digit random number
        zero = '0000'
        numo = str(random.choice(range(0,10000)))
        return "".join(j)+zero[0:4-len(numo)]+numo
    elif modde == 5 : # output: "yyyy-mm-dd-hh" if text = '-'
        return text[0].join(j[0:4])
    elif modde == 10 : # output: yyyymmdd
        return  ''.join( j[0:3] )

def path(glass,usrid=0,leve='usr'):
    pafa = ''
    if leve == 'opt':
        pafa = './database/opt/'+glass
    elif leve == 'usr':
        pafa = './database/usr/'+str(usrid)+'/'+glass
    subprocess.call(['mkdir','-p',pafa])
    return pafa+"/"

def ckpath(pafa,fille,addi='none'):
    subprocess.call(['mkdir','-p',pafa])
    try:
        alla = pprint.pformat(open(pafa+fille).read().splitlines())
    except FileNotFoundError:
        temp=open(pafa+fille,'w')
        if addi == 'json':
            json.dump({},temp)
        temp.close

def change(glass,target,id):
    if glass == "mode":
        os.system("mkdir -p ./database/usr/"+str(id)+"/"+target)
        aa=open("./database/usr/"+str(id)+"/mode","w")
        aa.write(target)
        aa.close()

def append(glass,id):
    if glass == "mode":
        aa=open("./database/usr/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()

def msg(type):
    return open("database/msg/"+type).read()

def uni(keywo):
    rsstr = ''
    for keno in keywo:
        try:
            keno.encode('latin-1')
            rsstr = rsstr + halfu.fullen(keno)
        except UnicodeEncodeError:
            rsstr = rsstr + keno
    return rsstr

def roundostr(numbe): # round() dos str
    numba = round(float(numbe),2)
    tamba = str(numba).split('.')
    tampa = ''
    if len(tamba[1]) != 2:
        tampa = '0'
    return str(numba)+tampa

def acedate(glass,modde,usrid=0,modda='check',desti='opt'):
    filla = modde + '.date'
    pafa = path(glass,usrid=usrid,leve=desti)
    ckpath(pafa,filla,addi='json')
    fillo = open(path(glass,usrid=usrid,leve=desti)+filla,'r')
    try:
        recod = json.load(fillo)
    except ValueError:
        recod = {}

    datte = recod.get('datte','00000000')

    if modda == 'write':
        recod.update({ 'datte' : date() })
        fillo = open(path(glass,usrid=usrid,leve=desti)+filla,'w')
        json.dump(recod,fillo)
        fillo.close()

    return datte
