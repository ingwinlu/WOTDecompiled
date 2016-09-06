# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralReferrerIntroWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralReferrerIntroWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onClickApplyButton(self):
        """
        :return :
        """
        self._printOverrideError('onClickApplyButton')

    def onClickHrefLink(self):
        """
        :return :
        """
        self._printOverrideError('onClickHrefLink')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/referralreferrerintrowindowmeta.pyc
