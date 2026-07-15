import re
# https://regexr.com/ (Best website to test regex)

text = "The quick brown fox jumps over the lazy dog. brown"

# search for a pattern
match = re.search('brown', text)
print(match)
if match:
    print('Match found!')
    print("start index: ", match.start())
    print('End Index: ', match.end())


matches = re.findall('the', text, re.IGNORECASE) # case insensitive search
print('Matches: ', matches)


new_text = re.sub('brown', 'red', text)
print('New Text: ', new_text)