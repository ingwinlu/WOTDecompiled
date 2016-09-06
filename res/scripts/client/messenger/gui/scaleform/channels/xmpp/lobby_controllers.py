# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/xmpp/lobby_controllers.py
import BigWorld
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import MessengerEvent
from messenger.formatters.users_messages import getBroadcastIsInCoolDownMessage
from messenger.gui.Scaleform.channels.layout import LobbyLayout
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.events import g_messengerEvents
from messenger.proto.xmpp.jid import makeContactJID
from messenger.proto.xmpp.messages.formatters import XmppLobbyMessageBuilder
from messenger.proto.xmpp.xmpp_constants import MESSAGE_LIMIT
_LAZY_EXIT_DELAY = 10.0

class _ChannelController(LobbyLayout):

    def __init__(self, channel, mBuilder=None):
        super(_ChannelController, self).__init__(channel, mBuilder or XmppLobbyMessageBuilder())
        self._hasUnreadMessages = False
        self.fireInitEvent()

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return None

    def canSendMessage(self):
        result, errorMsg = True, ''
        if self.proto.messages.isInCooldown():
            result, errorMsg = False, getBroadcastIsInCoolDownMessage(MESSAGE_LIMIT.COOLDOWN)
        return (result, errorMsg)

    def addMessage(self, message, doFormatting=True):
        activated = super(_ChannelController, self).addMessage(message, doFormatting)
        self._hasUnreadMessages = not activated
        return activated

    def hasUnreadMessages(self):
        return self._hasUnreadMessages and self._channel.getHistory()

    def _format(self, message, doFormatting=True):
        if not doFormatting:
            return message.text
        dbID = message.accountDBID
        return self._mBuilder.setGuiType(dbID).setRole(message.accountRole).setAffiliation(message.accountAffiliation).setName(dbID, message.accountName).setTime(message.sentAt).setText(message.body).build()

    def _onConnectStateChanged(self, _):
        if self._view:
            self._view.as_setJoinedS(self.isJoined())

    def _onMembersListChanged(self):
        self._refreshMembersDP()

    def _onMemberStatusChanged(self, _):
        self._refreshMembersDP()

    def _addListeners(self):
        self._channel.onConnectStateChanged += self._onConnectStateChanged
        self._channel.onMembersListChanged += self._onMembersListChanged
        self._channel.onMemberStatusChanged += self._onMemberStatusChanged

    def _removeListeners(self):
        self._channel.onConnectStateChanged -= self._onConnectStateChanged
        self._channel.onMembersListChanged -= self._onMembersListChanged
        self._channel.onMemberStatusChanged -= self._onMemberStatusChanged

    def _fireInitEvent(self):
        g_eventBus.handleEvent(MessengerEvent(MessengerEvent.LOBBY_CHANNEL_CTRL_INITED, {'controller': self}), scope=EVENT_BUS_SCOPE.LOBBY)

    def _fireDestroyEvent(self):
        g_eventBus.handleEvent(MessengerEvent(MessengerEvent.LOBBY_CHANNEL_CTRL_DESTROYED, {'controller': self}), scope=EVENT_BUS_SCOPE.LOBBY)


class ChatSessionController(_ChannelController):

    def __init__(self, channel, mBuilder=None):
        super(ChatSessionController, self).__init__(channel, mBuilder)
        self._isHistoryRqRequired = True

    def isJoined(self):
        return self._channel.isJoined() and not self._isHistoryRqRequired

    def activate(self):
        if self._isHistoryRqRequired:
            self.proto.messages.requestChatSessionHistory(self._channel.getID())
        super(ChatSessionController, self).activate()

    def exit(self):
        self.proto.messages.stopChatSession(self._channel.getID())

    def setHistory(self, history):
        super(ChatSessionController, self).setHistory(history)
        if self._isHistoryRqRequired:
            self._isHistoryRqRequired = False
            self._onConnectStateChanged(self._channel)

    def _addListeners(self):
        super(ChatSessionController, self)._addListeners()
        g_messengerEvents.users.onUserStatusUpdated += self.__onUserStatusUpdated

    def _removeListeners(self):
        g_messengerEvents.users.onUserStatusUpdated -= self.__onUserStatusUpdated
        super(ChatSessionController, self)._removeListeners()

    def _broadcast(self, message):
        self.proto.messages.sendChatMessage(self._channel.getID(), message)

    def __onUserStatusUpdated(self, user):
        if not user.isCurrentPlayer():
            if user.getProtoType() == PROTO_TYPE.XMPP:
                uid = user.getJID()
            else:
                uid = makeContactJID(user.getID())
            member = self._channel.getMember(uid)
            if member is not None:
                presence = user.getItem().getPresence()
                member.update(status=presence)
        return


class UserRoomController(_ChannelController):

    def exit(self):
        self.proto.messages.leaveFromMUC(self._channel.getID())

    def _addListeners(self):
        super(UserRoomController, self)._addListeners()
        events = g_messengerEvents.users
        events.onUsersListReceived += self.__me_onUsersListReceived
        events.onUserActionReceived += self.__me_onUserActionReceived

    def _removeListeners(self):
        events = g_messengerEvents.users
        events.onUsersListReceived -= self.__me_onUsersListReceived
        events.onUserActionReceived -= self.__me_onUserActionReceived
        super(UserRoomController, self)._removeListeners()

    def _broadcast(self, message):
        self.proto.messages.sendGroupChatMessage(self._channel.getID(), message)

    def __me_onUsersListReceived(self, _):
        self._refreshMembersDP()

    def __me_onUserActionReceived(self, _, contact):
        self._refreshMembersDP()


class LazyUserRoomController(_ChannelController):

    def __init__(self, channel):
        super(LazyUserRoomController, self).__init__(channel)
        self.__exitCallbackID = None
        return

    def activate(self):
        super(LazyUserRoomController, self).activate()
        self.__clearExitCallback()
        self.join()

    def deactivate(self, entryClosing=False):
        super(LazyUserRoomController, self).deactivate()
        self.__clearExitCallback()
        if not entryClosing:
            if self._channel.isJoined():
                self.__exitCallbackID = BigWorld.callback(_LAZY_EXIT_DELAY, self.__exitFromLazyChannel)
        else:
            self.__exitFromLazyChannel()

    def addMessage(self, message, doFormatting=True):
        return super(LazyUserRoomController, self).addMessage(message, doFormatting)

    def join(self):
        if not self._channel.isJoined():
            self.proto.messages.joinToMUC(self._channel.getID())

    def exit(self):
        self.proto.messages.leaveFromMUC(self._channel.getID())

    def _broadcast(self, message):
        self.proto.messages.sendGroupChatMessage(self._channel.getID(), message)

    def _fireInitEvent(self):
        g_eventBus.handleEvent(MessengerEvent(MessengerEvent.LAZY_CHANNEL_CTRL_INITED, {'controller': self}), scope=EVENT_BUS_SCOPE.LOBBY)

    def _fireDestroyEvent(self):
        g_eventBus.handleEvent(MessengerEvent(MessengerEvent.LAZY_CHANNEL_CTRL_DESTROYED, {'controller': self}), scope=EVENT_BUS_SCOPE.LOBBY)

    def __clearExitCallback(self):
        if self.__exitCallbackID is not None:
            BigWorld.cancelCallback(self.__exitCallbackID)
            self.__exitCallbackID = None
        return

    def __exitFromLazyChannel(self):
        self.__exitCallbackID = None
        if self._channel and self._channel.isJoined():
            self.exit()
        return
# okay decompiling ./res/scripts/client/messenger/gui/scaleform/channels/xmpp/lobby_controllers.pyc
