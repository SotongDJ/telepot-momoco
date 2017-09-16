import os
def id():
    sets=open("database/admin").read().split("=")
    return int(sets[1])

def user():
    #list a user list (return  a list of userid)
    os.system("ls database/usr --file-type -1 > database/usr/usrlist")
    lit=[]
    for lin in open("database/usr/usrlist").read().splitlines():
        if "/" in lin:
            lit.append(lin.replace("/",''))
    return lit
