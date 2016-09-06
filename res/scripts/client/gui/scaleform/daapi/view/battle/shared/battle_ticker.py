# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_ticker.py
from gui.Scaleform.daapi.view.common.BaseTicker import BaseTicker

class BattleTicker(BaseTicker):

    def __init__(self):
        super(BattleTicker, self).__init__()

    def _handleBrowserLink(self, link):
        """
        Battle ticker should not display a browser, so we will do nothing
        :param link: link to show
        """
        pass
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/battle/shared/battle_ticker.pyc
