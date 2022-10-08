# will create a list after performing some task

lis= [i+1 for i in range(20)]
lis2= [i for i in range(20) if i%2==0 if i%3==0   ]


print(lis,lis2)

lis3 =[i if i%2==0 else print('Invalid') for i in range(10)]


print(lis3)

#nested

lis4=[[i*j for j in range(10)] for i in range(10)]

print(lis4)