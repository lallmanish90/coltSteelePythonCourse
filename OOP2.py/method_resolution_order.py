"""
Multipule Resolution order

*whenever you create a class , python sets a Method Resolution
Order, or MRO, for that class, which is the order in which python
will look for methods on instances of that class
"""
# how to access the MRO is of a class
"""
* __mro__attribute on the class
*user the mro() method on the class
*use the built in help(cls) method
- the help(cls) method give back the most readable response
"""


class A:
    def do_somthing(self):
        print("method defined in: A")


class B(A):
    def do_somthing(self):
        print("method defined in: B")


class C(A):
    def do_somthing(self):
        print("method defined in: C")


class D(B, C):
    pass
    # def do_somthing(self):
    #     print("method defined in: D")


thing = D()
thing.do_somthing()
# print(D.__mro__)
# print(D.mro())
print(help(D))
