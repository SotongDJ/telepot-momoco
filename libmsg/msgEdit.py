"""msgEdit:
        main(temra,uuid,usrid)
        keyword(keywo)
        fin(uuid,usrid,libra)
        discar()"""

def main(temra,uuid):
    final="""Editing Card
——————————
ID: """+uuid+"""
Date: """+temra.get('datte','')+"""
Item: """+temra.get('namma','')+"""
Category: """+temra.get('klass','')+"""
Seller: """+temra.get('shoop','')+"""
　/change_Seller (or Agent)
　　——————　　
Spent from:
"""+temra.get('karen','')+" "+temra.get('price','')+' ('+temra.get('fromm','')+""")
　［Price (Account)］
　/change_Currency

　/change_Acc_From
　　——————　
Transfer to:
"""+temra.get('tkare','')+" "+temra.get('tpric','')+' ('+temra.get('toooo','')+""")
　［Price (Account)］
　/change_Currency_To

　/change_Acc_To
　　——————　　
"""+"""Notes:
"""+temra.get('desci','')+"""
——————————
　/Discard　/Save
"""
    return final

def keyword(keywo):
    final="""Filling the blank
——————————
Keyword:
　"""+keywo+"""

　/set_as_Date
(Format of Date: yyyy-mm-dd)
　/set_as_Item　/set_as_Category

　/set_as_Seller　/set_as_Notes
——————————
　/set_as_Account_From

　/set_as_Amount_From

　/set_as_Currency_Source
——————————
　/set_as_Account_To

　/set_as_Amount_To

　/set_as_Currency_Target
——————————
　/Discard　/Save
"""
    return final

def fin(uuid,usrid,libra):
    final="""Edited result
——————————
ID: """+uuid+"""
Date: """+libra['raw'][uuid].get('datte','')+"""
Item: """+libra['raw'][uuid].get('namma','')+"""
Category: """+libra['raw'][uuid].get('klass','')+"""
Seller: """+libra['raw'][uuid].get('shoop','')+"""
　　——————　　
Spent from:
"""+libra['raw'][uuid].get('karen','')+" "+libra['raw'][uuid].get('price','')+' ('+libra['raw'][uuid].get('fromm','')+""")
Transfer to:
"""+libra['raw'][uuid].get('tkare','')+" "+libra['raw'][uuid].get('tpric','')+' ('+libra['raw'][uuid].get('toooo','')+""")
　　——————　　
"""+"""Notes:
"""+libra['raw'][uuid].get('desci','')+"""
——————————
　/Back　/Edit
"""
    return final

def discar():
    final="""¡ Discard !
——————————

　Closed Editing Card

——————————
　/whats_now　/setting
"""
    return final
