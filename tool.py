import os
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
