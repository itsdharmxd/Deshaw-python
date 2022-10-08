
tup=(1,2,3,4,5,6,77,77)


print(tup[1])

for i in tup:
    print(i,end=' ')
print()


# tuples are  immutable
#  can delete  whole tuple but  not  a  single elements # but to couter this we can use sliceing and creating a new  tuples

print( tuple([12,3,4,4,5,6,6]) )


b=tup[:5]

print(b)