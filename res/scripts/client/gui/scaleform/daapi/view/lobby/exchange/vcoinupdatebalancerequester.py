# 2013.11.15 11:26:02 EST
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/exchange/VcoinUpdateBalanceRequester.py
import time
import BigWorld
import Event
from adisp import process
from gui.shared.utils.requesters import StatsRequester
import constants

class _VcoinUpdateBalanceRequester(object):

    def __init__(self):
        self.onEbankUpdateBalanceComplete = Event.Event()
        self.__buyCooldown = time.time()
        self.__buyCallback = None
        return

    def update(self, vcoin):
        if self.__buyCallback is None:
            self.__buyCallback = BigWorld.callback(max(self.__buyCooldown - time.time(), 0), lambda : self.__buyGold(int(vcoin)))
        return

    @process
    def __buyGold(self, vcoin):
        self.__buyCallback = None
        success, errStr = yield StatsRequester().ebankBuyGold(vcoin)
        self.__updateBuyingCooldown()
        self.onEbankUpdateBalanceComplete(errStr, vcoin)
        return

    def __updateBuyingCooldown(self):
        self.__buyCooldown = time.time() + constants.REQUEST_COOLDOWN.EBANK_BUY_GOLD

    def cancelBuyCallback(self):
        if self.__buyCallback is not None:
            BigWorld.cancelCallback(self.__buyCallback)
            self.__buyCallback = None
        return


g_instance = _VcoinUpdateBalanceRequester()
# okay decompyling res/scripts/client/gui/scaleform/daapi/view/lobby/exchange/vcoinupdatebalancerequester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.11.15 11:26:02 EST
