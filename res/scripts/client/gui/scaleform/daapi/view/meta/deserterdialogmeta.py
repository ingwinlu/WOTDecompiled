# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DeserterDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class DeserterDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    null
    """

    def as_setDataS(self, path, messageYOffset):
        """
        :param path:
        :param messageYOffset:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(path, messageYOffset)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/deserterdialogmeta.pyc
