# In the combination of args and kwargs we written args first then after kwargs.

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 6, jack = 56, marie = 89)