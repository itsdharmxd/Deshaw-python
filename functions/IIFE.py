from cProfile import label



# IIFE function
(lambda x:print(x) )(34)



# global variable


g=34445

def func():

    g=45
    print(  g,globals()['g']  )   #  function return dictionary of global variable


func()



# pass by  object refrence

