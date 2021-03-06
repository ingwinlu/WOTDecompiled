from debug_utils import LOG_ERROR, LOG_WARNING, LOG_DEBUG
from messenger.gui.Scaleform.channels import bw_factories
from messenger.gui.interfaces import IControllersCollection
from messenger.m_constants import PROTO_TYPE
from messenger.proto.events import g_messengerEvents
from messenger.storage import storage_getter

class ControllersCollection(IControllersCollection):

    def __init__(self, factories):
        super(ControllersCollection, self).__init__()
        self._factories = factories
        self._controllers = {}

    @storage_getter('channels')
    def channelsStorage(self):
        return None

    def init(self):
        self._addListeners()
        controllers = []
        for factory in self._factories.itervalues():
            controllers.extend(factory.init())

        self._controllers = dict(((ctrl.getChannel().getClientID(), ctrl) for ctrl in controllers))
        return controllers

    def clear(self):
        self._removeListener()
        for factory in self._factories.itervalues():
            factory.clear()

        self.removeControllers()

    def factory(self, channel):
        protoType = channel.getProtoType()
        controller = None
        if protoType in self._factories:
            controller = self._factories[protoType].factory(channel)
        else:
            LOG_ERROR('Controllers factory not found', protoType)
        return controller

    def getController(self, clientID):
        controller = None
        if clientID in self._controllers:
            controller = self._controllers[clientID]
        return controller

    def hasController(self, controller):
        return controller in self._controllers.values()

    def getControllerByCriteria(self, criteria):
        controller = None
        channel = self.channelsStorage.getChannelByCriteria(criteria)
        if channel:
            controller = self.getController(channel.getClientID())
        return controller

    def getControllersIterator(self):
        for controller in self._controllers.itervalues():
            yield controller

    def removeControllers(self):
        while len(self._controllers):
            _, controller = self._controllers.popitem()
            controller.clear()

    def _addListeners(self):
        channelsEvents = g_messengerEvents.channels
        channelsEvents.onChannelInited += self.__ce_onChannelInited
        channelsEvents.onChannelDestroyed += self.__ce_onChannelDestroyed

    def _removeListener(self):
        channelsEvents = g_messengerEvents.channels
        channelsEvents.onChannelInited -= self.__ce_onChannelInited
        channelsEvents.onChannelDestroyed -= self.__ce_onChannelDestroyed

    def _addController(self, channel):
        controller = None
        clientID = channel.getClientID()
        if not clientID:
            LOG_ERROR('Client ID for channel is not defined', channel)
            return
        else:
            if clientID is not self._controllers:
                controller = self.factory(channel)
                if controller is not None:
                    LOG_DEBUG('Channel controller is adding', channel)
                    self._controllers[channel.getClientID()] = controller
            else:
                LOG_WARNING('Controller already exists')
            return controller

    def _removeController(self, clientID):
        result = False
        if not clientID:
            LOG_ERROR('Client ID for channel is not defined')
            return False
        if clientID in self._controllers:
            LOG_DEBUG('Channel controller is deleting', clientID)
            self._controllers.pop(clientID).clear()
            result = True
        return result

    def __ce_onChannelInited(self, channel):
        self._addController(channel)

    def __ce_onChannelDestroyed(self, channel):
        self._removeController(channel.getClientID())


class LobbyControllers(ControllersCollection):

    def __init__(self):
        super(LobbyControllers, self).__init__({PROTO_TYPE.BW: bw_factories.LobbyControllersFactory()})


class BattleControllers(ControllersCollection):

    def __init__(self):
        super(BattleControllers, self).__init__({PROTO_TYPE.BW: bw_factories.BattleControllersFactory()})
