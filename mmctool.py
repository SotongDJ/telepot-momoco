import json, pprint
import tool, auth

def apmod(mode,text):
    mode.append(text)
    return mode

def ckmod(mode):
    modo = mode[-1]
    return modo

def chmod(mode):
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
