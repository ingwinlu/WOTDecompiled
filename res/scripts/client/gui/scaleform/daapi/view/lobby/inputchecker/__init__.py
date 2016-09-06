# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/inputChecker/__init__.py
from gui.Scaleform.daapi.view.lobby.inputChecker.InputChecker import InputChecker
from gui.Scaleform.framework import ViewTypes, ScopeTemplates, ViewSettings

class INPUT_CHECKER_ALIASES(object):
    INPUT_CHECKER = 'inputCheckerComponent'


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return (ViewSettings(INPUT_CHECKER_ALIASES.INPUT_CHECKER, InputChecker, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/lobby/inputchecker/__init__.pyc
