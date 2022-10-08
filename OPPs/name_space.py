# class  namespace

class names:
    data=34        # static member


a=names()

c=names()

b=names()

# class  namespace

names.data=100


print(names.data)

print(a.data)

print(b.data)

print(c.data)

print('\n\n')
# instance  namespace

a.data=101
print(names.data)

print(a.data)

print(b.data)

print(c.data)
