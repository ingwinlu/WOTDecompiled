# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/messenger/inject.py
from messenger import MessengerEntry

class messengerEntryProperty(property):

    def __get__(self, obj, objType=None):
        return MessengerEntry.g_instance


class channelsCtrlProperty(property):

    def __get__(self, obj, objType=None):
        return MessengerEntry.g_instance.gui.channelsCtrl
# okay decompiling ./res/scripts/client/messenger/inject.pyc
