# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactNoteManageViewMeta.py
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta

class ContactNoteManageViewMeta(BaseManageContactViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseManageContactViewMeta
    null
    """

    def sendData(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('sendData')

    def as_setUserPropsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setUserProps(value)
# okay decompiling ./res/scripts/client/messenger/gui/scaleform/meta/contactnotemanageviewmeta.pyc
