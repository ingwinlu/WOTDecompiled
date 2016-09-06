# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.py
from gui.Scaleform.daapi.view.meta.IconPriceDialogMeta import IconPriceDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n

class IconPriceDialog(IconPriceDialogMeta):

    def __init__(self, meta, handler):
        super(IconPriceDialog, self).__init__(meta, handler)

    def _populate(self):
        super(IconPriceDialog, self)._populate()
        self.as_setPriceLabelS(i18n.makeString(DIALOGS.REMOVECONFIRMATIONNOTREMOVABLEGOLD_MESSAGEPRICE))
        self.as_setMessagePriceS(self._meta.getMessagePrice(), 'gold', self._meta.getAction())
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/dialogs/iconpricedialog.pyc
