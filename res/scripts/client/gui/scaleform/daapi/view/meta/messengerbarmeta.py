# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MessengerBarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MessengerBarMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def channelButtonClick(self):
        """
        :return :
        """
        self._printOverrideError('channelButtonClick')

    def contactsButtonClick(self):
        """
        :return :
        """
        self._printOverrideError('contactsButtonClick')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/messengerbarmeta.pyc
