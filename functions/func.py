# closure is also present in python just  like JS


def add(a,b):
    c=a+b
    def addd(a,b):
        return a+b+c
    return addd



print (add(1,2)(4,5))


# key word argument

def sub(a,b):
    print(f" {a} {b} ")

sub(b=4,a=6)



# Variable lenght argument'


def names(*args):
    for i in args:
        print(i,end=' ')
names('dharmesh,upadhyay', 'lalit','upadhyaya')
print('')


# Key-value lenght argument

def namess(**kargs):
    for i in kargs.keys():
        print(kargs[i],end=' ')

namess(a=3,b=6,c=34,d=5)
