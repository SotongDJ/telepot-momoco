""" self.sender.sendMessage(mmcmsg.listMain(self._temra)) """
def main(datte,text):
    final="""Listing Card
——————————
Date:"""+datte+"""
List:
"""+text+"""
——————————
　/Choose_day　/Choose_month　/Choose_year
——————————
　/Close
"""
    return final

def change(keywo,text):
    final='Choose '+keywo+"""
——————————
List:
"""+text+"""
——————————
　/Back
"""
    return final

""" self.sender.sendMessage(mmcmsg.listSect(uuid,usrid,libra)) """
def single(uuid,usrid,libra):
    final="""Single record Card
——————————
ID: """+uuid+"""
Date: """+libra[uuid].get('datte','')+"""
Item: """+libra[uuid].get('namma','')+"""
Category: """+libra[uuid].get('klass','')+"""
Seller: """+libra[uuid].get('shoop','')+"""
　　——————　　
Spent from:
"""+libra[uuid].get('karen','')+" "+libra[uuid].get('price','')+' ('+libra[uuid].get('fromm','')+""")
Transfer to:
"""+libra[uuid].get('tkare','')+" "+libra[uuid].get('tpric','')+' ('+libra[uuid].get('toooo','')+""")
　　——————　　
"""+"""Notes:
"""+libra[uuid].get('desci','')+"""
——————————
　/Back　/Edit　/Delete　/setting
"""
    return final

""" self.sender.sendMessage(mmcmsg.listDisca()) """
def disca():
    final="""¡ Discard !
——————————

　Closed Listing Card

——————————
　/whats_now　/setting
"""
    return final
