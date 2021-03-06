#  Copyright (c) 2007, Enthought, Inc.
#  License: BSD Style.

# metadata.py --- Example of accessing trait metadata attributes

# --[Imports]-------------------------------------------------------------------
from __future__ import print_function
from traits.api import HasTraits, Int, List, Float, Instance, Any, TraitType


# --[Code]----------------------------------------------------------------------
class Foo(HasTraits):
    pass


class Test(HasTraits):
    i = Int(99)
    lf = List(Float)
    foo = Instance(Foo, ())
    any = Any([1, 2, 3])


# --[Example*]------------------------------------------------------------------
t = Test()

# Prints values of various metadata attributes for each of the traits.
print(t.trait("i").default)  # 99
print(t.trait("i").default_kind)  # value
print(t.trait("i").inner_traits)  # ()
print(t.trait("i").is_trait_type(Int))  # True
print(t.trait("i").is_trait_type(Float))  # False

print(t.trait("lf").default)  # []
print(t.trait("lf").default_kind)  # list
print(t.trait("lf").inner_traits)  # (<traits.traits.CTrait object at
#  0x01B24138>,)
print(t.trait("lf").is_trait_type(List))  # True
print(t.trait("lf").is_trait_type(TraitType))  # True
print(t.trait("lf").is_trait_type(Float))  # False
print(t.trait("lf").inner_traits[0].is_trait_type(Float))  # True

print(t.trait("foo").default)  # <undefined>
print(t.trait("foo").default_kind)  # factory
print(t.trait("foo").inner_traits)  # ()
print(t.trait("foo").is_trait_type(Instance))  # True
print(t.trait("foo").is_trait_type(List))  # False

print(t.trait("any").default)  # [1, 2, 3]
print(t.trait("any").default_kind)  # list
print(t.trait("any").inner_traits)  # ()
print(t.trait("any").is_trait_type(Any))  # True
print(t.trait("any").is_trait_type(List))  # False
