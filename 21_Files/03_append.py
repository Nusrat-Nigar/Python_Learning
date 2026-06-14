# Append to an existing file called John Doe.txt
# It should add data about John Doe's Hometown

f = open('John Doe.txt', 'a')

String = '''
John Doe initially live in Pheonix, Arizona. He is a very cool guy

'''

f.write(String)

f.close()