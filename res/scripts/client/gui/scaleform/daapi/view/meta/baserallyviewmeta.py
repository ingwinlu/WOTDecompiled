# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyView import AbstractRallyView

class BaseRallyViewMeta(AbstractRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractRallyView
    null
    """

    def as_setCoolDownS(self, value, requestId):
        """
        :param value:
        :param requestId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDown(value, requestId)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/baserallyviewmeta.pyc
