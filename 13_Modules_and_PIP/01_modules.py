# Two types of modules in Python:
# - Built in modules
# - External modules: this modules can either be written by us or they can also be installed using a utility called PIP
# List of all the built in modules: https://docs.python.org/3/py-modindex.html
import math
import myModule
import requests # this file has been savedby python installer behind the scenes. (run command: pip install requests)

print(math.sqrt(16))
myModule.hello()
r = requests.get('https://www.google.com')  # requests module is used to fetch the HTML of online pages
print(r.text)