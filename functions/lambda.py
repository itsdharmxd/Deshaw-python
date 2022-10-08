

# lambda function
sum =lambda x:(x+1,x+3)   # returning tuple

print(sum(4))

# nested lambda



add=lambda x:(lambda y:x+y)

print(add(3)(4))