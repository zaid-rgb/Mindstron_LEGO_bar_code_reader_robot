import unittest
from hamming_code import *
from stack_machine import *
from ctypes import c_ubyte


class TestHammingCode(unittest.TestCase):
    """ Please add your test cases here! """
    ham_obj = HammingCode()

    def test_decode(self):


        test_result_0 = self.ham_obj.decode((1, 1, 0, 1, 1, 1, 0, 0, 0, 0))
        self.assertEqual(((1, 1 ,0 ,1 ,0 ), HCResult.CORRECTED),test_result_0)



        test_result_1 = self.ham_obj.decode((0, 0, 1, 1, 0, 0, 0, 1, 1, 0))
        self.assertEqual(((None), HCResult.UNCORRECTABLE), test_result_1)

        test_result_2 = self.ham_obj.decode((1, 1, 1, 0, 1, 1, 0, 0, 1, 0))
        self.assertEqual(((1, 1, 1, 0, 1), HCResult.VALID), test_result_2)

        test_result_3 = self.ham_obj.decode((0, 0, 0, 0, 0, 0, 1, 1, 1, 0))
        self.assertEqual(((0, 0 ,0, 1 ,0), HCResult.CORRECTED), test_result_3)



class TestStackMachine(unittest.TestCase):

    stk_obj = StackMachine()


    def test_do(self):
        stackCheck = StackMachine()

        

        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 1, 0, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 0, 1, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 1, 0, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 0, 1, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 1, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 1, 0, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 1, 0, 0, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 1, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 1, 0, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 1, 0, 1, 1)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 1, 0, 1, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 1, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((1, 0, 0, 1, 0)))
        self.assertEqual(SMState.RUNNING, stackCheck.do((0, 0, 1, 1, 1)))  
        self.assertEqual(SMState.STOPPED, stackCheck.do((0, 0, 0, 0, 0)))  
              
        
        self.assertEqual((0, 0, 1, 1, 0, 0, 1, 0), stackCheck.top())








if __name__ == '__main':
    unittest.main()



