

# List vs Array
# list can have different type of data and not have a fix size

# List use more mermory

#importing only module
import array
arr=array.array('i',[1,2,3,4,5,6])
for i in arr:
    print(i,end=' ')



# importing all class  objects
from array import *

arr=array('i',[1,2,3,4,45,5])
print()
for i in arr:
    print(i,end=' ')

print()

# arr=array('i',[2.2,121,2,3,4,3,4])  # explicit typcasting needed  cannot done  by  python

# len()

print(len(arr))

arr.append(87654)

for i in arr:
    print(i,end=' ')





arr.pop()

# arr.remove(3)

arr.extend(arr)   # append another variable

for i in arr:
    print(i,end=' ')

print()



# Sliceing       [starting_index : (ending_index +1)]
for i in arr[1:5]:
    print(i,end=' ')

print()
#Slicing with optional start  and stop
for i in arr[4:]:
    print(i,end=' ')
print()
# Sliceing       [starting_index : (ending_index +1)]
for i in arr[-5:-1]:
    print(i,end=' ')



li=[1,2,3,4,5,6,7,8,9]

print(li[2:5])

print( li+li)

l2=li.copy()