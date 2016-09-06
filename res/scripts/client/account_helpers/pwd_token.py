# Python bytecode 2.7 (62211) disassembled from Python 2.7
# Embedded file name: scripts/client/account_helpers/pwd_token.py
from constants import DEFAULT_LANGUAGE
import hashlib
__all__ = ['generate']

def _generateMd5Hash(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


_BY_LANG = {'cn': _generateMd5Hash,
 'vn': _generateMd5Hash}

def generate(pwd):
    return pwd


if DEFAULT_LANGUAGE in _BY_LANG:
    generate = _BY_LANG[DEFAULT_LANGUAGE]
# okay decompiling ./res/scripts/client/account_helpers/pwd_token.pyc
