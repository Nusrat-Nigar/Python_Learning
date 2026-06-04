name = "Nusrat"
print(name[0:2]) # goes from 0 to 2-1

print(name[2:-1]) # same as name[2:5] 
                  # character index = [length of str + index] = [6+(-1) = 5]. It will print index 5 character.

# print(name[0:10:n])  # skip n-1 character
print(name[0:6:2])  # skip (2-1 = 1) character

print(name[:4])  # Replace the first empty number with 0  # name[0:4]
print(name[1:])  # Replace the last empty number with n-1, where n is length of string.  # name[1:6]