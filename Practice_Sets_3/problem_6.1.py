text = "The python programming is awesome"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"There are {count} vowels in the sentence")
