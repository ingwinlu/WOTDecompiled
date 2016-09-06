# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/login/__init__.py
from gui import GUI_SETTINGS
if GUI_SETTINGS.socialNetworkLogin['enabled']:
    from social_networks import Manager, SOCIAL_NETWORKS
    g_loginManager = Manager()
else:
    from Manager import Manager
    g_loginManager = Manager()
__all__ = ['g_loginManager']
# okay decompiling ./res/scripts/client/gui/login/__init__.pyc
