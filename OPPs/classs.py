import sys

# object  is the  base class  for all class  in python

# we pass self for binding puspose

# init methods  are  automatically called

from typing import overload


class ClassName(object):    # (object)  not mandatory

    names="Global name"   # class  instance just  like static variable

    @classmethod          # static or  class method      as a static method
    def cmethod(cls):
        print(cls.names)



    def __init__(s,value1,value2):    # s = self          as a constructor
        s.name=value1      # instance variable
        s.age=value2

    def display(s):             # we can ignore s hereb   as a method
        print(s.name)







cname=ClassName('dharmesh',22)

print(type(cname))

cname.display()

# instance variable

print(cname.name)


# class  method

print (ClassName.names)

print (cname.names)

print(ClassName.__name__)     # print name of any  class

#
print(__file__)


print(sys.path())

print(__doc__)