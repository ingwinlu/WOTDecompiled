# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/miniclient/fallout_controller.py
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitFalloutPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.fallout_controller', 'FalloutController', 'isAvailable', aspects=(_ParametrizeInitAspect,))
# okay decompiling ./res/scripts/client/gui/miniclient/fallout_controller.pyc
