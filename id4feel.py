import keywo
def idenFeel(msg):
    dicto=keywo.dicto("analisi/feel")
    dikta=keywo.dikta("analisi/feel")
    keywos=[]
    level=0
    limit=0.5
    for keyword in dicto.keys():
        print("keyword: "+keyword)
        if keyword in msg:
            level=level+dicto[keyword]
            keywos.append(keyword)
            print(keyword+"+"+str(dicto[keyword]))
    for keyword in dikta.keys():
        print("keyword: "+keyword)
        if keyword in msg:
            level=level*dikta[keyword]
            keywos.append(keyword)
            print(keyword+"*"+str(dikta[keyword]))
    #print("level="+str(level)+", limit="+str(limit))
    return {"level":level,"limit":limit,"keyword":keywos}
