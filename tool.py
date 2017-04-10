import os, time
def date(mode):
    a,b,c,d,e,f,g,h,i = time.localtime(time.time())
    j=[]
    for n in [a,b,c,d,e,f]:
        j.append(str(n))
    for n in range(1,6):
        if len(j[n]) == 1 :
            j[n]="0"+j[n]
    if mode == 0 : # output: ["yyyy","mm","dd","hh","mm","ss"]
        return j
    elif mode == 1 : # output: "yyyy-mm-dd"
        return "-".join(j[0:3])
    elif mode == 2 : # output: "yyyy-mm-dd hh:mm:ss"
        return "-".join(j[0:2])+" "+":".join(j[3:6])
    elif mode == 3 : # output: "yyyy-mm-dd hh:mm:ss"
        return "-".join(j[0:2])+" "+":".join(j[3:6])
    elif mode == 4 : # output: "yyyymmddhhmmss"
        return "".join(j)

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
