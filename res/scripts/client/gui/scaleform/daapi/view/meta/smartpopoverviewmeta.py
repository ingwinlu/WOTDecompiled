# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SmartPopOverViewMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView

class SmartPopOverViewMeta(AbstractPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractPopOverView
    null
    """

    def as_setPositionKeyPointS(self, valX, valY):
        """
        :param valX:
        :param valY:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPositionKeyPoint(valX, valY)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/smartpopoverviewmeta.pyc
