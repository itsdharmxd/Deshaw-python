import imp
from operator import imod
# from Pakages.cal.module_calculator import *    Not work for Pakages    <= WE CAN DO BY ADDING __add__ in __init__.py
from Pakages import *   #importing all modules from pakages only the defined one  like this  __all__=['module_calculator'] in __init__.py of package

print(module_calculator.add(3,4))