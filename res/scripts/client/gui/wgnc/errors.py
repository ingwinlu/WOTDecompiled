# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/gui/wgnc/errors.py


class ParseError(Exception):

    def __init__(self, *args, **kwargs):
        super(ParseError, self).__init__(*args, **kwargs)


class ValidationError(Exception):

    def __init__(self, *args, **kwargs):
        super(ValidationError, self).__init__(*args, **kwargs)
# okay decompiling ./res/scripts/client/gui/wgnc/errors.pyc
