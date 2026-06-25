words = ['Python', 'Rocks', 'Ai', 'Abs']

lengths = [n for w in words if(n := len(w)) < 4]
print(lengths)