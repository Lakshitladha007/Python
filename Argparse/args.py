def demo_function(normal, *args):

    for item in args:
        print(normal)
        print(item)

    print(type(args))

demo_function(300, *["hello", "lakshit", 22])

""" It is just a convetion, we can also write anything instead of args, the only 
thing is it should have * in front of it.
example:
def demo_function(normal, *argsrohan):

    for item in argsrohan:
        print(normal)
        print(item)

    print(type(args))

demo_function(300, *["hello", "lakshit", 22])

"""

# It is a thumb rule that in our function definition at first "normal" arguements come, 
# than "args" and at last "kargs"