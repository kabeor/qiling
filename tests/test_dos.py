#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import os, random, sys, unittest

import string as st
from binascii import unhexlify

sys.path.insert(0, "..")

from qiling import *
from qiling.const import *
from qiling.exception import *
from qiling.os.windows.fncc import *
from qiling.os.windows.utils import *
from unicorn.x86_const import *

class DOSTest(unittest.TestCase):

    def test_dos_8086_hello(self):
        ql = Qiling(["../examples/rootfs/8086/dos/HI.DOS_COM"], "../examples/rootfs/8086/dos")
        ql.run()
        del ql

if __name__ == "__main__":
    unittest.main()