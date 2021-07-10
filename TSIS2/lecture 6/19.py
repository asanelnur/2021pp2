def myfunc(a):
        def square(b):
                nonlocal a
                a ** 2
                return a*b
        return square
func= myfunc(4)
print(func(4))