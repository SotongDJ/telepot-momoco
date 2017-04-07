import os
def path(pylum,id):
    os.system("mkdir -p ./database/usr/"+str(id)+"/"+pylum)
    return "./database/usr/"+str(id)+"/"+pylum+"/"

def check(pylum,id):
    if pylum == "mode":
        aa=open("./database/usr/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()
        bb=open("./database/usr/"+str(id)+"/mode").read().splitlines()[0].replace("--","")
        return bb

def change(pylum,target,id):
    if pylum == "mode":
        os.system("mkdir -p ./database/usr/"+str(id)+"/"+target)
        aa=open("./database/usr/"+str(id)+"/mode","w")
        aa.write(target)
        aa.close()

def append(pylum,id):
    if pylum == "mode":
        aa=open("./database/usr/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()

def msg(type):
    return open("database/msg/"+type).read()
