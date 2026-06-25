class MathUtils:

    @staticmethod
    def add(a, b):
        return a+b
    
    @classmethod
    def description(cls):
        print(f'This is the utility class for math operation')


# Calling with object creation
e = MathUtils()
print(e.add(6, 9))
e.description()


# Calling with class Name
print(MathUtils.add(3,9))
MathUtils.description()