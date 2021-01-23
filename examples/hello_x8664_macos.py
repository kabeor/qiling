#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import sys
sys.path.append("..")
from qiling import *

if __name__ == "__main__":
    ql = Qiling(["rootfs/x8664_macos/bin/x8664_hello"], "rootfs/x8664_macos", output = "debug")
    ql.run()
