#!/usr/bin/env python3
from typeconstraints import typeconstraints,ARRAYOF,NONNABLE,ANYOF
import unittest

class typeconstraintsTest(unittest.TestCase):

    def testbaseok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    def testbasenok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, "hi", 42)
    def testbaservalnok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return "I don't think so"
        self.assertRaises(AssertionError, foo, "hi", 42)
    def testarrayof01(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertTrue(foo([1,3,5,8],"hi"))
    def testarrayof02(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, [1,3,5,8.6], "hi")
    def testarrayof03(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, [1,3,"ho",19], "hi")
    def testarrayof04(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, 199, "hi")
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    def testnonnable02(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st=None):
            return True
        self.assertTrue(foo(42))
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, 42, False)
    def testanyoff01(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    def testanyoff02(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,3.1415926))
    def testanyoff03(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, 42, 199)

if __name__ == "__main__":
    unittest.main()
