import os

a = os.listdir('dir')
print(a)

print(os.getcwd())  # current directory in which we are working

print(os.path.exists('dir')) 

os.remove('sample.txt')  # it will remove the sample.txt file 

os.rmdir('dir') # it will only remove the empty directory.To remove the non-empty directory we use shutil method