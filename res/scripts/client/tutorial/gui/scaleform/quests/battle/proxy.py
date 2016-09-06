# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/battle/proxy.py
from tutorial.gui import GUIProxy

class BattleQuestsProxy(GUIProxy):

    def __init__(self):
        super(BattleQuestsProxy, self).__init__()

    def init(self):
        self.onGUILoaded()
        return True

    def clear(self):
        self.clearChapterInfo()

    def getSceneID(self):
        return 'Battle'

    def playEffect(self, effectName, args, itemRef=None, containerRef=None):
        return False

    def isEffectRunning(self, effectName, effectID=None):
        return False
# okay decompiling ./res/scripts/client/tutorial/gui/scaleform/quests/battle/proxy.pyc
