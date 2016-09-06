# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/VoiceChatManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class VoiceChatManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def isPlayerSpeaking(self, accountDBID):
        """
        :param accountDBID:
        :return Boolean:
        """
        self._printOverrideError('isPlayerSpeaking')

    def isVivox(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isVivox')

    def isYY(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isYY')

    def isVOIPEnabled(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isVOIPEnabled')

    def as_onPlayerSpeakS(self, accountDBID, isSpeak, isHimseljoinUnitButtonf):
        """
        :param accountDBID:
        :param isSpeak:
        :param isHimseljoinUnitButtonf:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onPlayerSpeak(accountDBID, isSpeak, isHimseljoinUnitButtonf)
# okay decompiling ./res/scripts/client/gui/scaleform/framework/entities/abstract/voicechatmanagermeta.pyc
