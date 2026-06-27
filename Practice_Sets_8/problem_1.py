# 1st way
f = open('notes.txt', 'r')
content = f.read()
print(content)
f.close()


# 2nd way
with open('note.txt', 'w') as f:
    f.write('Learning python is fun!')