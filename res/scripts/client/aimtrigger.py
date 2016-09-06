# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/AimTrigger.py
import BigWorld
import TriggersManager

class AimTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AIM, name=self.name, position=self.position, radius=self.radius, maxDistance=self.maxDistance)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
# okay decompiling ./res/scripts/client/aimtrigger.pyc
