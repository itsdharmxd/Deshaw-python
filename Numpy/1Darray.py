import numpy

arr=[8,7,5,4,3,2]

print(type(arr))

for i in arr:
    print(i,end=' ')
else :
    print(' ')

# array using array function

arr = numpy.array([2,3,4,5,6,45,7,8,8,7],float);
arr[0]=345678
for i in arr:
    print(i,end=' ')
print( '')


# array using linspace

arr=numpy.linspace(1,8,num=7,endpoint=False)

for i in arr:
    print(i,end=' ')
print('')

# array using Logspace

arr=numpy.logspace(1,8,num=7,endpoint=False)




# arange

arr=  numpy.arange(1.1,45,0.3)   # we can give float as argument in arange

for i in arr:
    print(i,end=' ')
print()

arr=arr+5   # every element increment by 5

arr=arr+arr



# any( ) and all( )  function

arr=numpy.array(  [1,2,3,4,5,6])
arr2=numpy.array(  [1,2,3,8,9,0])

c=all( arr+arr2)

d=any( arr+arr2)

print(c,d)


# Deep Copy
d=arr.copy()
d= numpy.copy(arr)