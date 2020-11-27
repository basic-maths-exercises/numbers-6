import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for i in range(20) :
            val = np.random.randint(1,9999)
            arr = convertToHex(val) 
            for j in range(5) : 
               ppp = 16**(4-j)
               vv = int(np.floor( val / ppp ) )
               val = val - vv*ppp
               strv=str(vv)
               if vv==10 : strv = "A"
               elif vv==11 : strv = "B"
               elif vv==12 : strv = "C"
               elif vv==13 : strv = "D" 
               elif vv==14 : strv = "E"
               elif vv==15 : strv = "F"
               self.assertTrue( strv==arr[4-j], "The function is not working" )
