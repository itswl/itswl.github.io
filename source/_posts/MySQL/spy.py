import requests

a = requests.get('https://segmentfault.com/a/1190000013746118')

print(a.text)