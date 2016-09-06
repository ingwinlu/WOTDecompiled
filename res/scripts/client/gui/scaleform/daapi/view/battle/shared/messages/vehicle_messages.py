# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/vehicle_messages.py
from MemoryCriticalController import g_critMemHandler
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
from gui.battle_control import g_sessionProvider
from gui.shared.events import GameEvent
from helpers import i18n
from items import vehicles

class VehicleMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleMessages, self).__init__('VehicleMessagesPanel', 'vehicle_messages_panel.xml')

    def __del__(self):
        LOG_DEBUG('VehicleMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleMessages, self)._addGameListeners()
        self.addListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        for message in g_critMemHandler.messages:
            self.__handleMemoryCriticalMessage(message)

        g_critMemHandler.onMemCrit += self.__handleMemoryCriticalMessage
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode += self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey += self.__onShowVehicleMessageByKey
            ctrl.onUIPopulated()
        return

    def _removeGameListeners(self):
        self.removeListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        g_critMemHandler.onMemCrit -= self.__handleMemoryCriticalMessage
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode -= self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey -= self.__onShowVehicleMessageByKey
        super(VehicleMessages, self)._removeGameListeners()
        return

    def __handleMemoryCriticalMessage(self, message):
        self.showMessage(message[1])

    def __handleScreenShotMade(self, event):
        if 'path' not in event.ctx:
            return
        self.showMessage('SCREENSHOT_CREATED', {'path': i18n.encodeUtf8(event.ctx['path'])})

    def __onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID):
        LOG_DEBUG('onShowVehicleMessage', code, postfix, entityID, extra, equipmentID)
        names = {'device': '',
         'entity': '',
         'target': ''}
        if extra is not None:
            names['device'] = extra.deviceUserString
        if entityID:
            names['entity'] = g_sessionProvider.getCtx().getPlayerFullName(entityID)
        if equipmentID:
            equipment = vehicles.g_cache.equipments().get(equipmentID)
            if equipment is not None:
                postfix = '_'.join((postfix, equipment.name.split('_')[0].upper()))
        self.showMessage(code, names, postfix=postfix)
        return

    def __onShowVehicleMessageByKey(self, key, args=None, extra=None):
        self.showMessage(key, args, extra)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/battle/shared/messages/vehicle_messages.pyc
