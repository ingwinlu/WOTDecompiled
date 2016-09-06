# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CursorMeta.py
from gui.Scaleform.framework.entities.View import View

class CursorMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def as_setCursorS(self, cursor):
        """
        :param cursor:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCursor(cursor)

    def as_showCursorS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showCursor()

    def as_hideCursorS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideCursor()
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/cursormeta.pyc
