import os, time, random
def date(mode,text):
    a,b,c,d,e,f,g,h,i = time.localtime(time.time())
    j=[]
    for n in [a,b,c,d,e,f]:
        j.append(str(n))
    for n in range(1,6):
        if len(j[n]) == 1 :
            j[n]="0"+j[n]
    if mode == 0 : # output: ["yyyy","mm","dd","hh","mm","ss"]
        return j
    elif mode == 1 : # output: "yyyy-mm-dd" if text = '-'
        return text.join(j[0:3])
    elif mode == 2 : # output: "yyyy-mm-dd hh:mm:ss" if text = '-:'
        return text[0].join(j[0:2])+" "+text[1].join(j[3:6])
    elif mode == 3 : # output: "yyyymmddhhmmss"
        return "".join(j)+text
    elif mode == 4 : # output: "yyyymmddhhmmssrrrrrrrr" rrrr is eight digit random number
        zero = '0000'
        numo = str(random.choice(range(0,10000)))
        return "".join(j)+zero[0:4-len(numo)]+numo


def path(glass,id):
    os.system("mkdir -p ./database/usr/"+str(id)+"/"+glass)
    return "./database/usr/"+str(id)+"/"+glass+"/"

def check(glass,id):
    if glass == "mode":
        aa=open("./database/usr/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()
        bb=open("./database/usr/"+str(id)+"/mode").read().splitlines()[0].replace("--","")
        return bb

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
