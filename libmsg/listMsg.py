""" self.sender.sendMessage(mmcmsg.listMain(self._temra)) """
def main(datte,text):
    final="""Listing Card
----------------------------
Date:"""+datte+"""
List:
"""+text+"""
----------------------------
  /Choose_day /Choose_month  /Choose_year
----------------------------
  /Close
"""
    return final

def change(keywo,text):
    final='Choose '+keywo+"""
----------------------------
List:

"""+text+"""
----------------------------
  /Back
"""
    return final

""" self.sender.sendMessage(mmcmsg.listSect(uuid,usrid,libra)) """
def single(uuid,usrid,libra):
    final="""Single record Card
----------------------------
ID: """+uuid+"""
Date: """+libra['raw'][uuid]["datte"]+"""
Item: """+libra['raw'][uuid]["namma"]+"""
Category: """+libra['raw'][uuid]["klass"]+"""
Seller: """+libra['raw'][uuid]["shoop"]+"""
"""+"""

Spent from which Account:
"""+libra['raw'][uuid]["fromm"]+' ('+libra['raw'][uuid]["karen"]+" "+libra['raw'][uuid]["price"]+""")
Transfer to which Account:
"""+libra['raw'][uuid]["toooo"]+' ('+libra['raw'][uuid]["tkare"]+" "+libra['raw'][uuid]["tpric"]+""")

"""+"""Notes:
"""+libra['raw'][uuid]["desci"]+"""
----------------------------
   /Back  /Edit  /Delete  /setting

"""
    return final

""" self.sender.sendMessage(mmcmsg.listDisca()) """
def disca():
    final="""¡ Discard !
----------------------------

  Closed Listing Card

----------------------------
  /whats_now  /setting
"""
    return final
