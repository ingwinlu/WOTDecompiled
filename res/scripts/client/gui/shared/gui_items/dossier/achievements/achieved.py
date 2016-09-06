# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/Achieved.py
from abstract import RegularAchievement
from gui.shared.gui_items.dossier.achievements import validators

class Achieved(RegularAchievement):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompiling ./res/scripts/client/gui/shared/gui_items/dossier/achievements/achieved.pyc
