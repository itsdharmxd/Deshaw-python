

dic={n:n*2  for n in range (10) if n%2==0 if n%3==0}
print(dic)


dic={n:(n if  n%2==0 else 'Invalid')  for n in range (10) if n%2==0 if n%3==0}

