from chat_shared import CHAT_RESPONSES
from debug_utils import LOG_ERROR, LOG_DEBUG
from messenger.proto.bw import filters, errors
from messenger.proto.bw.ChannelsManager import ChannelsManager
from messenger.proto.bw.ChatActionsListener import ChatActionsListener
from messenger.proto.bw.ClanListener import ClanListener
from messenger.proto.bw.ServiceChannelManager import ServiceChannelManager
from messenger.proto.bw.UsersManager import UsersManager
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import IProtoPlugin

class BWProtoPlugin(ChatActionsListener, IProtoPlugin):

    def __init__(self):
        super(BWProtoPlugin, self).__init__()
        self.__isConnected = False
        self.channels = ChannelsManager()
        self.users = UsersManager()
        self.clanListener = ClanListener()
        self.serviceChannel = ServiceChannelManager()

    def clear(self):
        self.__isConnected = False
        self._removeChatActionsListeners()
        self.channels.clear()
        self.users.clear()
        self.serviceChannel.clear()
        self.clanListener.stop()

    def connect(self, scope):
        if not self.__isConnected:
            self.__isConnected = True
            self._addChatActionsListeners()
            self.clanListener.start()
            self.__isConnected = True
        self.channels.switch(scope)
        self.users.switch(scope)
        self.serviceChannel.switch(scope)

    def disconnect(self):
        self.serviceChannel.clear()
        if self.__isConnected:
            self.clear()

    def onChatActionFailure(self, chatAction):
        actionResponse = CHAT_RESPONSES[chatAction['actionResponse']]
        LOG_DEBUG('onChatActionFailure', dict(chatAction))
        for name in ('channels', 'users'):
            manager = getattr(self, name)
            if manager.handleChatActionFailureEvent(actionResponse, dict(chatAction)):
                return

        responseProcessor = self.__errorsHandlers.get(actionResponse, self.__defaultErrorHandler)
        if hasattr(self, responseProcessor):
            getattr(self, responseProcessor)(chatAction)
        else:
            LOG_ERROR('onChatActionFailure: response processor for response %s(%s) not registered' % (actionResponse, actionResponse.index()))

    def _addChatActionsListeners(self):
        self.channels.addListeners()
        self.users.addListeners()
        self.serviceChannel.addListeners()

    def _removeChatActionsListeners(self):
        self.removeAllListeners()
        self.channels.removeAllListeners()
        self.users.removeAllListeners()
        self.serviceChannel.removeAllListeners()

    __errorsHandlers = {CHAT_RESPONSES.channelNotExists: '_BWProtoPlugin__onChannelNotExists',
     CHAT_RESPONSES.memberBanned: '_BWProtoPlugin__onMemberBanned',
     CHAT_RESPONSES.chatBanned: '_BWProtoPlugin__onChatBanned',
     CHAT_RESPONSES.actionInCooldown: '_BWProtoPlugin__passError',
     CHAT_RESPONSES.commandInCooldown: '_BWProtoPlugin__onCommandInCooldown',
     CHAT_RESPONSES.inviteCommandError: '_BWProtoPlugin__passError',
     CHAT_RESPONSES.inviteCreateError: '_BWProtoPlugin__passError',
     CHAT_RESPONSES.inviteCreationNotAllowed: '_BWProtoPlugin__passError'}
    __defaultErrorHandler = '_BWProtoPlugin__onActionFailure'

    def __onMemberBanned(self, chatAction):
        error = errors.MemberBannedError.create(chatAction)
        if error:
            g_messengerEvents.onServerErrorReceived(error)

    def __onChatBanned(self, chatAction):
        error = errors.ChatBannedError.create(chatAction)
        if error:
            g_messengerEvents.onServerErrorReceived(error)

    def __onCommandInCooldown(self, chatAction):
        error = errors.CommandInCooldownError.create(chatAction)
        if error:
            g_messengerEvents.onServerErrorReceived(error)

    def __onActionFailure(self, chatAction):
        error = errors.ChatActionError.create(chatAction)
        if error:
            g_messengerEvents.onServerErrorReceived(error)

    def __passError(self, chatAction):
        pass
