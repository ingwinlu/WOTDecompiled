# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/VOIP/__init__.py
import BigWorld

def getVOIPManager():
    if not globals().has_key('__handler'):
        from VOIPManager import VOIPManager
        globals()['__handler'] = VOIPManager()
        BigWorld.VOIP.setHandler(__handler)
    return __handler
# okay decompiling ./res/scripts/client/voip/__init__.pyc
