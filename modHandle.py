from core import tool
from core import modDatabase
from core import modSearch
from core import modVariables

from msgMain import MsgMain
from msgShort import MsgShort
"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from open_chat_message() in momocobot.py.
"""

class Hande:
    """ handle received msg
    pass command to excute() for futher action (which is more complex)
    change cache info that store in memory (arg)
    and reply back to user
    """
    def __init__(self,msg,argo):
        self.text = msg
        self.argo = argo

        self.resut = []
        self.cos = 0

        msgMain = MsgMain(self.argo.lingua)

        if self.argo.primo == ['']:
            self.resut = [msgMain.home({'keywo':self.text})]
