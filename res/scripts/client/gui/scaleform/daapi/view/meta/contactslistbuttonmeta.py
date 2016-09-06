# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ContactsListButtonMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsListButtonMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setContactsCountS(self, num):
        """
        :param num:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContactsCount(num)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/contactslistbuttonmeta.pyc
