# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileSummaryViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileSummaryViewMeta(ClanProfileBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanProfileBaseView
    null
    """

    def hyperLinkGotoMap(self):
        """
        :return :
        """
        self._printOverrideError('hyperLinkGotoMap')

    def hyperLinkGotoDetailsMap(self):
        """
        :return :
        """
        self._printOverrideError('hyperLinkGotoDetailsMap')

    def sendRequestHandler(self):
        """
        :return :
        """
        self._printOverrideError('sendRequestHandler')

    def as_updateStatusS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateStatus(data)

    def as_updateGeneralBlockS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneralBlock(data)

    def as_updateFortBlockS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFortBlock(data)

    def as_updateGlobalMapBlockS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateGlobalMapBlock(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/clanprofilesummaryviewmeta.pyc