# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/LobbyChannelWindowMeta.py
from messenger.gui.Scaleform.view.lobby.SimpleChannelWindow import SimpleChannelWindow

class LobbyChannelWindowMeta(SimpleChannelWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleChannelWindow
    null
    """

    def as_getMembersDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getMembersDP()

    def as_hideMembersListS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideMembersList()
# okay decompiling ./res/scripts/client/messenger/gui/scaleform/meta/lobbychannelwindowmeta.pyc
