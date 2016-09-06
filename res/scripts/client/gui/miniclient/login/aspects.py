# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/miniclient/login/aspects.py
from helpers import aop

class ShowBGInsteadVideo(aop.Aspect):

    def __init__(self):
        super(ShowBGInsteadVideo, self).__init__()

    def atCall(self, cd):
        super(ShowBGInsteadVideo, self).atCall(cd)
        cd.self._showOnlyStaticBackground()
        cd.avoid()
# okay decompiling ./res/scripts/client/gui/miniclient/login/aspects.pyc
