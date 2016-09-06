# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/OfflineEntity.py
import BigWorld

class OfflineEntity(BigWorld.Entity):

    def __init__(self):
        pass

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        pass

    def onLeaveWorld(self):
        pass

    def collideSegment(self, startPoint, endPoint, skipGun=False):
        pass


class PlayerOfflineEntity(BigWorld.Entity):

    def __init__(self):
        pass

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        pass

    def onLeaveWorld(self):
        pass

    def handleKeyEvent(self, event):
        return False
# okay decompiling ./res/scripts/client/offlineentity.pyc
