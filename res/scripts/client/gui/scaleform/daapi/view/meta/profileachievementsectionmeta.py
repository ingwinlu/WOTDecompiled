# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileAchievementSectionMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileAchievementSectionMeta(ProfileSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSection
    null
    """

    def as_setRareAchievementDataS(self, rareID, rareIconId):
        """
        :param rareID:
        :param rareIconId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRareAchievementData(rareID, rareIconId)
# okay decompiling ./res/scripts/client/gui/scaleform/daapi/view/meta/profileachievementsectionmeta.pyc
