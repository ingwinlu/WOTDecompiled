# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBaseScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutBaseScorePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_initS(self, maxValue, warningValue):
        """
        :param maxValue:
        :param warningValue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(maxValue, warningValue)

    def as_playScoreHighlightAnimS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_playScoreHighlightAnim()

    def as_stopScoreHighlightAnimS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_stopScoreHighlightAnim()
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/falloutbasescorepanelmeta.pyc
