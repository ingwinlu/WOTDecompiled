# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/Vibroeffects/Controllers/OnceController.py
import BigWorld
from Vibroeffects import VibroManager
from debug_utils import *

class OnceController:

    def __init__(self, effectName, gain=100):
        VibroManager.g_instance.launchQuickEffect(effectName, 1, gain)
# okay decompiling ./res/scripts/client/vibroeffects/controllers/oncecontroller.pyc
