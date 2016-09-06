# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/miniclient/login/pointcuts.py
import aspects
from helpers import aop

class ShowBGInsteadVideo(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.login.LoginView', 'LoginView', '_showBackground', aspects=(aspects.ShowBGInsteadVideo,))
# okay decompiling ./res/scripts/client/gui/miniclient/login/pointcuts.pyc
