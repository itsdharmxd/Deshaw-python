# Hello Python
# OPPs language
# High Level , Interpreted , Platform Independent ,Huge Library ,scalable
# case sensitive


#  WORKING OF PYTHON






print('Hello'+" Dharmesh")

print('dharmesh','upadhyay')

# in C and JAVA address is of variable
# but in python address is of value

a=10
print(id(a))  # id() return address
print (type(a))  # type() return address
# VARIABLE => dynamic


#string
str='dharmesh'
str="dharmesh"

#array
arr=[1,2,3,4,5,'dharmesh']

print(arr[-1])
arr[-1]=45

#tuple

tup=(3,4,5,6)
print(type(tup))
print(tup[-1])
# tup[-1]= 34    cannot assign on tuple


#Range      (start , end, steps to take)
ran=range(5,0,-2)

for i in ran:
    print(i)

print(ran)

#Set            unordered /not accessable with index

se={3,4,5,6,7,8,56}
print(type(se))


# Map

ma={"a":'sadfgh',"b":'sadfgh',"c":'sadfgh',"d":'sadfgh'}
print(type(ma))
for i in ma.keys():
    print(ma[i])

#re-assign with other data type
a=10
a='dharmesh'
a,b,c,d=1,2,3,4

print(a,b,c,d)

#operators

print(5/2)  # floor division

print(5//2)  # integer division

print(5**2) # power

print(9**(1/2))  #sqrt

print(5%2) #modulus

True
False

# Logical operator   => and or not

print (True and True)

print (True or True)

print( not True)


print(True and 11 and 45)  # First false value otherwise  last value
print(False or 11 or NULL)   # First  true value else give 0



# Bitwise operator

print (1 & 0)

print (1 | 0)

print (~0)

print(5<<1)

print(1^0)

# in operator

print('ar ' in  "Dharmesh")

print('ar ' not in  "Dharmesh")



# is operator   return true when both location are same

print (10 is '10')
print(10 == '10')

print (10 is not '10')
print(10 != '10')


# implicit and explicit type conversion (implicit type conversion done by Python it self as it dont do data loss)

a=int(5/2)
print (a)


# bin()  return binary

print(bin(4))




# print('dharmesh' +34)
# print(22+34+'Dharmesh')

# INPUT / OUTPUT

print( int( input('enter a number')))

