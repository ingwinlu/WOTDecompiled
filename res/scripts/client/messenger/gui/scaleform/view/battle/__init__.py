# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/battle/__init__.py
from gui.Scaleform.framework import ViewTypes, ViewSettings, ScopeTemplates

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from messenger.gui.Scaleform.view.battle import messenger_view
    from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
    return (ViewSettings(BATTLE_VIEW_ALIASES.BATTLE_MESSENGER, messenger_view.BattleMessengerView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()
# okay decompiling ./res/scripts/client/messenger/gui/scaleform/view/battle/__init__.pyc
