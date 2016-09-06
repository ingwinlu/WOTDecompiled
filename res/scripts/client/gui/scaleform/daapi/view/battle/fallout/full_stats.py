# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/full_stats.py
from gui.Scaleform.daapi.view.meta.FCStatsMeta import FCStatsMeta
from gui.Scaleform.daapi.view.meta.FMStatsMeta import FMStatsMeta
from gui.battle_control import g_sessionProvider

class FalloutClassicFullStats(FCStatsMeta):
    pass


class FalloutMultiTeamFullStats(FMStatsMeta):

    def _populate(self):
        super(FalloutMultiTeamFullStats, self)._populate()
        self.as_setSubTypeS(g_sessionProvider.getArenaDP().getMultiTeamsType())
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/battle/fallout/full_stats.pyc
