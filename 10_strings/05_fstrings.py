# string formatting
template = "Dear {}, you are awesome. Take this {}$ bag"
a = 'John'
a1 = 10000

s1 = template.format(a, a1)
print(s1)

# how fstring works
print(f"{a} you are awesome and take this {a1}$ bag")