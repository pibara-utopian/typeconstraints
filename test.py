#!/usr/bin/env python3
from typeconstraints import typeconstraints

class ToTo(object):
    def false(self):
        return False

class BoBo(object):
    def false(self):
        return True

def checkfalse(arg):
    return arg.false() == False

@typeconstraints([int,str,checkfalse,bool])
def bar(baz,foo,f,optional=False):
    print(foo,baz*baz)

bar(199,"OK",ToTo())
bar(17,"SHOULD FAIL",f=BoBo(),optional=True)
