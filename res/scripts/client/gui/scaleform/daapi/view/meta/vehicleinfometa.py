# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleInfoMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getVehicleInfo(self):
        """
        :return :
        """
        self._printOverrideError('getVehicleInfo')

    def onCancelClick(self):
        """
        :return :
        """
        self._printOverrideError('onCancelClick')

    def as_setVehicleInfoS(self, vehicleInfo):
        """
        :param vehicleInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleInfo(vehicleInfo)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/vehicleinfometa.pyc
