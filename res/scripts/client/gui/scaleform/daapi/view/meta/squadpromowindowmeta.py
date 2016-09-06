# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadPromoWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class SquadPromoWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    null
    """

    def onHyperlinkClick(self):
        """
        :return :
        """
        self._printOverrideError('onHyperlinkClick')

    def as_setHyperlinkS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHyperlink(label)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/squadpromowindowmeta.pyc
