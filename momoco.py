import tool, json

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
def chmod(num,mode,text):
    if num == 0:
        mode.append(text)
        return mode
    elif num == 1:
        try:
            mode.pop()
            return mode
        except IndexError:
            print("IndexError: pop from empty list")
            return mode
    else:
        print("Missing mode_num")


def check(file_name):
    a=open(file_name,"r")
    b=json.load(a)
    for n in b.keys():
        print(n)
        for m in b[n].keys():
            print("    "+m+" : "+b[n][m])
