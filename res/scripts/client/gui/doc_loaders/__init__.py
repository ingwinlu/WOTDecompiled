# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/doc_loaders/__init__.py
from items import _xml

def readDict(xmlCtx, section, subsectionName, converter=lambda value: value.asString):
    result = {}
    for name, value in _xml.getChildren(xmlCtx, section, subsectionName):
        result[name] = converter(value)

    return result
# okay decompiling ./res/scripts/client/gui/doc_loaders/__init__.pyc
