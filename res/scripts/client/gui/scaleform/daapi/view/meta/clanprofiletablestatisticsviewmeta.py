# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileTableStatisticsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileTableStatisticsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAdditionalTextS(self, visible, text):
        """
        :param visible:
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalText(visible, text)

    def as_getDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/clanprofiletablestatisticsviewmeta.pyc
