
def decor(fun):
    def inner ():
        print('before ')
        fun()
        print('after')
    return inner


@decor   # @<function name> which is decorating
def num():
    print("num func")
    print('end')


  #privoiusly
# decor(num)()    after @<function name>

#we can directly call

# now
num()
