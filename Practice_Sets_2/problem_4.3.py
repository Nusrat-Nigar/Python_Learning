num = int(input("Enter a number: "))
sum = 0
while num!=0:
    rem = num%10
    sum = sum*10 + rem
    num //= 10

print(sum)

# using advance slicing
'''
num = int(input("Enter a number: "))
print(int(str(num)[::-1]))

'''