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
