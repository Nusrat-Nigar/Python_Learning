import requests
r = requests.get('https://api.github.com/users/Nusrat-Nigar')
# print(r.text)

with open("Nusrat.txt", "w") as f:
    f.write(r.text)
