# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def quitBattleClick(self):
        """
        :return :
        """
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        """
        :return :
        """
        self._printOverrideError('settingsClick')

    def helpClick(self):
        """
        :return :
        """
        self._printOverrideError('helpClick')

    def cancelClick(self):
        """
        :return :
        """
        self._printOverrideError('cancelClick')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        """
        :param serverName:
        :param tooltipFullData:
        :param serverState:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)

    def as_setServerStatsS(self, stats, tooltipType):
        """
        :param stats:
        :param tooltipType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/ingamemenumeta.pyc
