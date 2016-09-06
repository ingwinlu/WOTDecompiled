# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/shared/utils/requesters/parsers/Parser.py


class Parser(object):

    @staticmethod
    def parseVehicles(data):
        return data

    @staticmethod
    def parseModules(data, type):
        return data

    @staticmethod
    def getParser(itemTypeID):
        if itemTypeID == 1:
            return Parser.parseVehicles
        return lambda data: Parser.parseModules(data, itemTypeID)
# okay decompiling ./res/scripts/client/gui/shared/utils/requesters/parsers/parser.pyc
