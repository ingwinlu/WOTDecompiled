# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameHelpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameHelpWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def clickSettingWindow(self):
        """
        :return :
        """
        self._printOverrideError('clickSettingWindow')

    def as_setKeysS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setKeys(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/ingamehelpwindowmeta.pyc
