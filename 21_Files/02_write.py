# Write to a file called John Doe.txt
# It should contain data about John

f = open('John Doe.txt', 'w')

String = '''
John Doe is a nice guy. He lives in Nyc and he works with python
His faourite package is Pandas

'''

f.write(String)

f.close()