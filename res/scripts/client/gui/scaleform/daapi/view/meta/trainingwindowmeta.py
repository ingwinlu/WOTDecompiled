# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TrainingWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def updateTrainingRoom(self, key, time, isPrivate, description):
        """
        :param key:
        :param time:
        :param isPrivate:
        :param description:
        :return :
        """
        self._printOverrideError('updateTrainingRoom')

    def as_setDataS(self, info, mapsData):
        """
        :param info:
        :param mapsData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(info, mapsData)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/trainingwindowmeta.pyc
