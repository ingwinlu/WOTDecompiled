# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/battle_timer.py
from gui.Scaleform.daapi.view.battle.shared.battle_timers import BattleTimer
FALLOUT_ENDING_SOON_TIME = 120

class FalloutBattleTimer(BattleTimer):

    def __init__(self):
        super(FalloutBattleTimer, self).__init__()

    def _getEndingSoonTime(self):
        return FALLOUT_ENDING_SOON_TIME
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/battle/fallout/battle_timer.pyc
