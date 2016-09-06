# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconPriceDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.IconDialog import IconDialog

class IconPriceDialogMeta(IconDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends IconDialog
    null
    """

    def as_setMessagePriceS(self, price, currency, actionPriceData):
        """
        :param price:
        :param currency:
        :param actionPriceData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagePrice(price, currency, actionPriceData)

    def as_setPriceLabelS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPriceLabel(label)

    def as_setOperationAllowedS(self, isAllowed):
        """
        :param isAllowed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOperationAllowed(isAllowed)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/iconpricedialogmeta.pyc
