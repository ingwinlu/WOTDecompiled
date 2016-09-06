# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TickerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TickerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showBrowser(self, entryID):
        """
        :param entryID:
        :return :
        """
        self._printOverrideError('showBrowser')

    def as_setItemsS(self, items):
        """
        :param items:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/tickermeta.pyc
