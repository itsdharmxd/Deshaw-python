
from operator import truediv


li=[1,2,3,4,5,6,7,8,9,78]          # original



def h_marks(n):
    if( n>=6):
        return True

li2=filter(h_marks,li)

for i in li2:
    print(i,end=' ')

print('erftgh')


li3=list( map(lambda x:x+5,li))

print(li3)

for i in li3:
    print(i,end=' ')

