

from dis import dis


def disp(a,b):
    yield a
    yield b



gen= disp(10,12)
print(type(gen))
print(next(gen))
print(next(gen))


