# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/eliteWindow/EliteWindow.py
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO
from gui.Scaleform.daapi.view.meta.EliteWindowMeta import EliteWindowMeta
from gui.shared import g_itemsCache

class EliteWindow(EliteWindowMeta):

    def __init__(self, ctx=None):
        super(EliteWindow, self).__init__()
        self.vehInvID = ctx['vehTypeCompDescr']

    def _populate(self):
        super(EliteWindow, self)._populate()
        self.as_setVehicleS(makeVehicleVO(g_itemsCache.items.getItemByCD(self.vehInvID)))

    def onWindowClose(self):
        self.destroy()
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/lobby/elitewindow/elitewindow.pyc
