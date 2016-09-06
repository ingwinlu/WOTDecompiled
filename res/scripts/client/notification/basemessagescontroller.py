# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/notification/BaseMessagesController.py


class BaseMessagesController(object):

    def __init__(self, model):
        self._model = model

    def cleanUp(self):
        self._model = None
        return
# okay decompiling ./res/scripts/client/notification/basemessagescontroller.pyc
