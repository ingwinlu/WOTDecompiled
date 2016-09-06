# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/sounds/sound_systems/no_system.py
from gui.sounds.abstract import SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems

class NoSoundSystem(SoundSystemAbstract):

    def getID(self):
        return SoundSystems.UNKNOWN
# okay decompiling ./res/scripts/client/gui/sounds/sound_systems/no_system.pyc
