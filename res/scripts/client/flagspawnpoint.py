# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/FlagSpawnPoint.py
import BigWorld
from debug_utils import LOG_DEBUG

class FlagSpawnPoint(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('FlagSpawnPoint ', self.position)
# okay decompiling ./res/scripts/client/flagspawnpoint.pyc
