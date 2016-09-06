# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ConquerorAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import ClassProgressAchievement
from abstract.mixins import Fortification

class ConquerorAchievement(Fortification, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, 'conqueror', _AB.FORT, dossier, value)

    def getNextLevelInfo(self):
        return ('fortDefResLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, 'conqueror')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFortMiscStats().getLootInSorties()
# okay decompiling ./res/scripts/client/gui/shared/gui_items/dossier/achievements/conquerorachievement.pyc
