import requests
text = requests.get("https://api.github.com")
print(text.json())