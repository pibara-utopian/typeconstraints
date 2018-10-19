#!/usr/bin/env python3
from typeconstraints import typeconstraints,ARRAYOF,NONNABLE,ANYOF,MIXEDARRAY,MIXEDDICT
import unittest

class typeconstraintsTest(unittest.TestCase):

    # Positive test for type constraint with plain types
    def testbaseok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    # Negative test for type constraints with plain types, swapped function argument types.
    def testbasenok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, "hi", 42)
    # Negative test for type constraints with plain types, function returns wrong type
    def testbaservalnok(self):
        @typeconstraints([int,str],[bool])
        def foo(num,st):
            return "I don't think so"
        self.assertRaises(AssertionError, foo, "hi", 42)
    # Positive test with an argument that is an list of elements of some type.
    def testarrayof01(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertTrue(foo([1,3,5,8],"hi"))
    # Negative test with an argument that is an list of elements of some type. One element has wrong type.
    def testarrayof02(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, [1,3,5,8.6], "hi")
    # Negative test with an argument that is an list of elements of some type. One element has wrong type.
    def testarrayof03(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, [1,3,"ho",19], "hi")
    # Negative test with an argument that is an list of elements of some type. Called with string instead of list.
    def testarrayof04(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo(arr1,st):
            return True
        self.assertRaises(AssertionError, foo, 199, "hi")
    # Possitive test with argument that is allowed to be specified as None. First with a regular value.
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    # Possitive test with argument that is allowed to be specified as None. Now with a None value.
    def testnonnable02(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st=None):
            return True
        self.assertTrue(foo(42))
    # Negative test with argument that is allowed to be specified as None. Wrong type used.
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, 42, False)
    # Positive test with argument that is allowed to be one from a collection of types. Use first allowed type.
    def testanyoff01(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,"hi"))
    # Positive test with argument that is allowed to be one from a collection of types. Use second allowed type.
    def testanyoff02(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertTrue(foo(42,3.1415926))
    # Negative test with argument that is allowed to be one from a collection of types. Use invalid type.
    def testanyoff03(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo(num,st):
            return True
        self.assertRaises(AssertionError, foo, 42, 199)
    # Positive test with a list that is composed of a fixed series of non-equal typed values.
    def testmixedarray01(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float])],[bool])
        def foo(num,arr):
            return True
        self.assertTrue(foo(42,["hi",42,3.1415927]))
    # Positive test with a list that is composed of a fixed series of non-equal typed values, padded with fixed type values.
    def testmixedarray02(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo(num,arr):
            return True
        self.assertTrue(foo(42,["hi",42,3.1415927,1.8,1.0]))
    # Negative test with a list that is composed of a fixed series of non-equal typed values.To many pad values.
    def testmixedarray03(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo(num,arr):
            return True
        self.assertRaises(AssertionError, foo, 42, ["hi",42,3.1415927,1.8,1.0,7.4,19.11,123.45])
    # Negative test with a list that is composed of a fixed series of non-equal typed values. Wrong type pad arguments.
    def testmixedarray04(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=str)],[bool])
        def foo(num,arr):
            return True
        self.assertRaises(AssertionError,foo, 42, ["hi",42,3.1415927,1.8,1.0])
    # Negative test with a list that is composed of a fixed series of non-equal typed values. Wrong non-pad argument type.
    def testmixedarray05(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo(num,arr):
            return True
        self.assertRaises(AssertionError, foo, 42, ["hi",42.8,3.1415927])
    # Positive test with a dict that is composed of a fixed set of named typed members.
    def testmixeddict01(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool})])
        def foo(num,dct):
            return True
        self.assertTrue(foo(42,{"bar": "Bushmills", "baz": 3.1415927, "qux": False}))
    # Negative test with a dict that is composed of a fixed set of named typed members.
    def testmixeddict02(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool})])
        def foo(num,dct):
            return True
        self.assertRaises(AssertionError, foo, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": 17})
    # Positive test with a dict that is composed of a fixed set of named typed members. Optional.
    def testmixeddict03(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},optionals=["qux"])])
        def foo(num,dct):
            return True
        self.assertTrue(foo(42,{"bar": "Bushmills", "baz": 3.1415927}))
    # Negative test with a dict that is composed of a fixed set of named typed members. Optional of wrong type
    def testmixeddict04(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},optionals=["qux"])])
        def foo(num,dct):
            return True
        self.assertRaises(AssertionError, foo, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": 17}, optionals=["qux"])
    # Positive test with a dict that is composed of a fixed set of named typed members. Extra unspecified field.
    def testmixeddict05(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},ignore_extra=True)])
        def foo(num,dct):
            return True
        self.assertTrue(foo(42,{"bar": "Bushmills", "baz": 3.1415927, "qux": False, "quux": 17}))
    # Negative test with a dict that is composed of a fixed set of named typed members. Extra unspecified field.
    def testmixeddict06(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},ignore_extra=False)])
        def foo(num,dct):
            return True
        self.assertRaises(AssertionError, foo, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": False, "quux": 17})

   #MIXEDDICT({"foo": str,"bar": float},ignore\_extra=True,optionals=["bar"])
if __name__ == "__main__":
    unittest.main()
