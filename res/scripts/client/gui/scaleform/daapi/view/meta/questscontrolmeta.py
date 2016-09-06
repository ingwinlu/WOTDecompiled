# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsControlMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsControlMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showQuestsWindow(self):
        """
        :return :
        """
        self._printOverrideError('showQuestsWindow')

    def as_isShowAlertIconS(self, value, highlight):
        """
        :param value:
        :param highlight:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isShowAlertIcon(value, highlight)

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/questscontrolmeta.pyc
