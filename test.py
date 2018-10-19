#!/usr/bin/env python3
from typeconstraints import typeconstraints,ARRAYOF,NONNABLE,ANYOF,MIXEDARRAY,MIXEDDICT
import unittest

class typeconstraintsTest(unittest.TestCase):

    # Positive test for type constraint with plain types
    def testbaseok(self):
        @typeconstraints([int,str],[bool])
        def foo01(num,st):
            return True
        self.assertTrue(foo01(42,"hi"))
    # Negative test for type constraints with plain types, swapped function argument types.
    def testbasenok(self):
        @typeconstraints([int,str],[bool])
        def foo02(num,st):
            return True
        self.assertRaises(AssertionError, foo02, "hi", 42)
    # Negative test for type constraints with plain types, function returns wrong type
    def testbaservalnok(self):
        @typeconstraints([int,str],[bool])
        def foo03(num,st):
            return "I don't think so"
        self.assertRaises(AssertionError, foo03, "hi", 42)
    # Positive test with an argument that is an list of elements of some type.
    def testarrayof01(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo04(arr1,st):
            return True
        self.assertTrue(foo04([1,3,5,8],"hi"))
    # Negative test with an argument that is an list of elements of some type. One element has wrong type.
    def testarrayof02(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo05(arr1,st):
            return True
        self.assertRaises(AssertionError, foo05, [1,3,5,8.6], "hi")
    # Negative test with an argument that is an list of elements of some type. One element has wrong type.
    def testarrayof03(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo06(arr1,st):
            return True
        self.assertRaises(AssertionError, foo06, [1,3,"ho",19], "hi")
    # Negative test with an argument that is an list of elements of some type. Called with string instead of list.
    def testarrayof04(self):
        @typeconstraints([ARRAYOF(int),str],[bool])
        def foo07(arr1,st):
            return True
        self.assertRaises(AssertionError, foo07, 199, "hi")
    # Possitive test with argument that is allowed to be specified as None. First with a regular value.
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo08(num,st):
            return True
        self.assertTrue(foo08(42,"hi"))
    # Possitive test with argument that is allowed to be specified as None. Now with a None value.
    def testnonnable02(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo09(num,st=None):
            return True
        self.assertTrue(foo09(42))
    # Negative test with argument that is allowed to be specified as None. Wrong type used.
    def testnonnable01(self):
        @typeconstraints([int,NONNABLE(str)],[bool])
        def foo10(num,st):
            return True
        self.assertRaises(AssertionError, foo10, 42, False)
    # Positive test with argument that is allowed to be one from a collection of types. Use first allowed type.
    def testanyoff01(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo11(num,st):
            return True
        self.assertTrue(foo11(42,"hi"))
    # Positive test with argument that is allowed to be one from a collection of types. Use second allowed type.
    def testanyoff02(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo12(num,st):
            return True
        self.assertTrue(foo12(42,3.1415926))
    # Negative test with argument that is allowed to be one from a collection of types. Use invalid type.
    def testanyoff03(self):
        @typeconstraints([int,ANYOF([str,float])],[bool])
        def foo13(num,st):
            return True
        self.assertRaises(AssertionError, foo13, 42, 199)
    # Positive test with a list that is composed of a fixed series of non-equal typed values.
    def testmixedarray01(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float])],[bool])
        def foo14(num,arr):
            return True
        self.assertTrue(foo14(42,["hi",42,3.1415927]))
    # Positive test with a list that is composed of a fixed series of non-equal typed values, padded with fixed type values.
    def testmixedarray02(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo15(num,arr):
            return True
        self.assertTrue(foo15(42,["hi",42,3.1415927,1.8,1.0]))
    # Negative test with a list that is composed of a fixed series of non-equal typed values.To many pad values.
    def testmixedarray03(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo16(num,arr):
            return True
        self.assertRaises(AssertionError, foo16, 42, ["hi",42,3.1415927,1.8,1.0,7.4,19.11,123.45])
    # Negative test with a list that is composed of a fixed series of non-equal typed values. Wrong type pad arguments.
    def testmixedarray04(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=str)],[bool])
        def foo17(num,arr):
            return True
        self.assertRaises(AssertionError,foo17, 42, ["hi",42,3.1415927,1.8,1.0])
    # Negative test with a list that is composed of a fixed series of non-equal typed values. Wrong non-pad argument type.
    def testmixedarray05(self):
        @typeconstraints([int,MIXEDARRAY([str,int,float],maxsize=6,pad_type=float)],[bool])
        def foo18(num,arr):
            return True
        self.assertRaises(AssertionError, foo18, 42, ["hi",42.8,3.1415927])
    # Positive test with a dict that is composed of a fixed set of named typed members.
    def testmixeddict01(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool})])
        def foo19(num,dct):
            return True
        self.assertTrue(foo19(42,{"bar": "Bushmills", "baz": 3.1415927, "qux": False}))
    # Negative test with a dict that is composed of a fixed set of named typed members.
    def testmixeddict02(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool})])
        def foo20(num,dct):
            return True
        self.assertRaises(AssertionError, foo20, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": 17})
    # Positive test with a dict that is composed of a fixed set of named typed members. Optional.
    def testmixeddict03(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},optionals=["qux"])])
        def foo21(num,dct):
            return True
        self.assertTrue(foo21(42,{"bar": "Bushmills", "baz": 3.1415927}))
    # Negative test with a dict that is composed of a fixed set of named typed members. Optional of wrong type
    def testmixeddict04(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},optionals=["qux"])])
        def foo22(num,dct):
            return True
        self.assertRaises(AssertionError, foo22, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": 17}, optionals=["qux"])
    # Positive test with a dict that is composed of a fixed set of named typed members. Extra unspecified field.
    def testmixeddict05(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},ignore_extra=True)])
        def foo23(num,dct):
            return True
        self.assertTrue(foo23(42,{"bar": "Bushmills", "baz": 3.1415927, "qux": False, "quux": 17}))
    # Negative test with a dict that is composed of a fixed set of named typed members. Extra unspecified field.
    def testmixeddict06(self):
        @typeconstraints([int,MIXEDDICT({"bar": str, "baz": float, "qux": bool},ignore_extra=False)])
        def foo24(num,dct):
            return True
        self.assertRaises(AssertionError, foo24, 42, {"bar": "Bushmills", "baz": 3.1415927, "qux": False, "quux": 17})
    def testcomplex01(self):
        @typeconstraints([
                int,
                ARRAYOF(
                    ARRAYOF(
                        MIXEDDICT(
                            {
                                "foo": str,
                                "bar": ANYOF([int,float]),
                                "baz": NONNABLE(bool)
                            }
                        )
                    )
                )
        ])
        def foo25(num,dct):
            return True
        self.assertTrue(foo25(42,
            [
                [
                    {"foo": "bilbo", "bar": 17, "baz": True},
                    {"foo": "frodo", "bar": 3.1414926, "baz": False}
                ],
                [
                    {"foo": "peppin", "bar": 11, "baz": None}
                ]
            ]
        ))
    def testcomplex02(self):
        @typeconstraints([
                int,
                ARRAYOF(
                    ARRAYOF(
                        MIXEDDICT(
                            {
                                "foo": str,
                                "bar": ANYOF([int,float]),
                                "baz": NONNABLE(bool)
                            }
                        )
                    )
                )
        ])
        def foo25(num,dct):
            return True
        self.assertRaises(
                AssertionError,
                foo25,
                42,
                [
                    [
                        {"foo": "bilbo", "bar": 17, "baz": True},
                        {"foo": "frodo", "bar": 3.1414926, "baz": False}
                    ],
                    [
                        {"foo": "peppin", "bar": 11, "baz": "NOTGOOD"}
                    ]
                ]
        )
if __name__ == "__main__":
    unittest.main()
