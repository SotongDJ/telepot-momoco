import os
def admin(id):
    if id == int(open("database/admin").read()):
        return True
    else:
        return False

def check():
    if id == str(open("database/admin").read()):
        return "Admin id is: "+open("database/admin").read()
    else:
        return "No permision"

def id():
    return open("database/admin").read()

def user():
    #list a user list (return  a list of userid)
    os.system("ls database/usr --file-type -1 > database/usr/usrlist")
    lit=[]
    for lin in open("database/usr/usrlist").read().splitlines():
        if "/" in lin:
            lit.append(lin.replace("/",''))
    return lit
