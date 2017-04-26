import tool, json, pprint

"""--------------------------------------------------------
        self._mod=momoco.chmod(mode_num,self._mod,mode_text)
            mode_num
                = 0
                    change mode to mode_text
                = 1
                    change mode back to previous
            self._mod = []
            mode_text = ""
"""
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
    pprint(b)
