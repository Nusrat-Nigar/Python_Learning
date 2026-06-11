marks = {'Nusrat':34, 'jack':78, 'Lily': 45}

print(marks.keys())

print(marks.values())

print(marks.items())

for key, value in marks.items():
    print(key, value)

# find the name with the highest marks
highest_marks_name = max(marks, key = marks.get)
print(highest_marks_name)

marks.pop('jack') # remove 'jack' key
print(marks)

marks.clear() # empty dictionary
print(marks)

