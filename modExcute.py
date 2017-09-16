import tool, modDatabase, modSearch, modVariables
"""
This is the main part of Momocobot to handle income msg
and reply required msg back to user.

The codes of this file mainly lineage from comme() in momocobot.py.
"""

def excut(msg={},arg={}):
    """ process  msg
    grab command from hande()
    assign task to other mod
    and reply result back to hande()
    """
    resut=[]
    cos=0
    return {'resut':resut, 'arg':arg, 'cos':cos}
