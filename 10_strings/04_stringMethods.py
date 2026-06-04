name  = "Hello World"  # Strings are immutable
# name[0] = "R"  # you can't change it

print(len(name))

print(name.upper(), name) # means original string is not change 

print(name.lower())

print(name.capitalize())  # capatilizes the first character of the string only (like Hello world)

print(name.title()) # first character of every world will be capital letter (like Hello World)

text = '  hello world  '

print(text.strip())  # output: "hello world"

print(text.lstrip())  # output: "hello world  "

print(text.rstrip())  # output: "  hello world"

text1 = "Python is fun"
print(text1.find('is'))   # index of first occurence
print(text1.replace('fun', 'awesome'))  # replace all occurences of fun with awesome


fruits = "Apples, Bananas, PineApples"
print(fruits.split(","))

print(",".join(['Apples', ' Bananas', ' PineApples']))

alphanum = "python12453"
print(alphanum.isalpha())  # output: False
print(alphanum.isdigit())  # output: False 
print(alphanum.isalnum())  # output: True
print(alphanum.isspace())  # output: False

# character encoding
print(ord('A'))
print(chr(67))
