# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortChoiceDivisionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortChoiceDivisionWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def selectedDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('selectedDivision')

    def changedDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('changedDivision')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/fortchoicedivisionwindowmeta.pyc
