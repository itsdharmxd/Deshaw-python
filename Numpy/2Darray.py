row,col=5,5


  #default value=1 here
arr=[[[1]*col]*col]*row

print(arr)
for i in range (row):
    for j in range(col):
        print(arr[i][j],end=' ')
    print()


# Slicing 2D array

print(arr[0:3 ])