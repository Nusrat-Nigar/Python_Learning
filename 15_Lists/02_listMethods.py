marks = [34, 56, 46, 89, 24]
extra_marks = [32, 36, 96]

marks.append(63)  # this will change the original list
print(marks)

marks.pop() # remove last item from the list
print(marks)

marks.extend(extra_marks)
print(marks)

marks.remove(56)
print(marks)

marks.reverse()
print(marks)

marks.sort()
print(marks)

# sort the list in decending order
marks.sort(reverse=True)
print(marks)

decending_order = sorted(marks, reverse=True)
print(decending_order)

marks.insert(1,33)
print(marks)

