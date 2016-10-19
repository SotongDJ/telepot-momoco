import os
def path(pylum,id):
    os.system("mkdir -p ./database/"+str(id)+"/"+pylum)
    return "./database/"+str(id)+"/"+pylum+"/"

def check(pylum,id):
    if pylum == "mode":
        aa=open("./database/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()
        bb=open("./database/"+str(id)+"/mode").read().splitlines()[0].replace("--","")
        return bb

def change(pylum,target,id):
    if pylum == "mode":
        os.system("mkdir -p ./database/"+str(id)+"/"+target)
        aa=open("./database/"+str(id)+"/mode","w")
        aa.write(target)
        aa.close()

def append(pylum,id):
    if pylum == "mode":
        aa=open("./database/"+str(id)+"/mode","a")
        aa.write("--")
        aa.close()

def msg(type):
    return open("database/msg/"+type).read()
