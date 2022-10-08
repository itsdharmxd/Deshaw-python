i=0
while(i<5):
    print(i,end=' ')
    i+=1


print()

# for loop
for i in range(0,5,1):
    print(i,end=' ')
    i+=1

i=0


# while with else
while i<5:
    print(i)
    i+=1
    if(i==3):
        break
else:                    # runs only when whole loop has run not partially
    print('else')


a=range(5)
print( type(a),a[0],a[2])
# a[2]=45  not support


str='dharmesh'

for i in str:
    print(i)
    if(i=='r'):
        break

else:                  # runs when loop runs completely and not partiallly
    print('for else')



# pass statement     we can write this if we dont want to write any thing in block

if True:
    print('pass')
    pass
    print('pass 2')
else :
    print('dharmesh')