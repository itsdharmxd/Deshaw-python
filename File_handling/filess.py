

from distutils.file_util import write_file
from fileinput import close
from genericpath import isfile
from operator import imod
import os
#f==file
#open(filename,mode,buffering,encoding,errors,newline,closefd,opener)
f=open('dharmesh.txt','r+')


print(isfile('dharmesh.txt'))
print(os.path.isfile('dharmesh.txt'))  #  inside OS module
#file object variables

# read

print(f.read(5))
print(f.readline())


# write
f.write("My name  is dharmesh")
f.writelines(['s','s','s'])





print(f.name)

print(f.mode)

print(f.closed)  # isClosed()

print(f.readable)  # isReadable()

print(f.writable())







#  garbage collector can also close  if you did not  
# but that is not a right way

f.close()

