# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/doc_loaders/GuiDirReader.py
import ResMgr

class GuiDirReader(object):
    SCALEFORM_STARTUP_VIDEO_PATH = 'gui/flash/video'
    SCALEFORM_STARTUP_VIDEO_MASK = 'video/%s'
    VIDEO_EXTENSION = 'usm'

    def __init__(self):
        super(GuiDirReader, self).__init__()

    @staticmethod
    def getAvailableIntroVideoFiles():
        ds = ResMgr.openSection(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH)
        movieFiles = []
        for filename in ds.keys():
            basename, extension = filename.split('.')
            if extension == GuiDirReader.VIDEO_EXTENSION and basename[0:1] != '_':
                movieFiles.append(GuiDirReader.SCALEFORM_STARTUP_VIDEO_MASK % filename)

        ResMgr.purge(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH, True)
        return movieFiles
# okay decompiling ./res/scripts/client/gui/doc_loaders/guidirreader.pyc
