def sum_of_digit(num):
   if num==0:
      return 0
   
   return num%10 + sum_of_digit(num//10)

n = int(input("Enter the number: "))
print(sum_of_digit(n))