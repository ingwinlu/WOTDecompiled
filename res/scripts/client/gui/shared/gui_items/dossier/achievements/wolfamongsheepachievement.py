# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WolfAmongSheepAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class WolfAmongSheepAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value=None):
        super(WolfAmongSheepAchievement, self).__init__('wolfAmongSheepMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'wolfAmongSheep')
# okay decompiling ./res/scripts/client/gui/shared/gui_items/dossier/achievements/wolfamongsheepachievement.pyc
