try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        inputs, outputs = [], [] 
        for i in range(20) :
            val, ov = np.random.randint(1,9999), []
            inputs.append((val,))
            for j in range(5) : 
               ppp = 16**(4-j)
               vv = np.floor( val / ppp )
               val = val - vv*ppp
               if vv==10 : ov.append("A")
               elif vv==11 : ov.append("B")
               elif vv==12 : ov.append("C")
               elif vv==13 : ov.append("D") 
               elif vv==14 : ov.append("E")
               elif vv==15 : ov.append("F")
               else : ov.append( str(vv) )
            outputs.append(ov)
        assert( fc.check_func('convertToHex', inputs, outputs ) )
