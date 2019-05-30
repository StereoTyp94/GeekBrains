# вводите url, в результате получаете список ссылок с указанного url
import requests, re

res = []
pattrn = r'<a.*href=.?(\w|-)*://((\w|-)+\.[\w\.-]+)'
file = requests.get(input())
with open('input.txt', 'w') as f:
    f.write(file.text)
with open('input.txt') as f:
    for l in f.readlines():
        ur = re.findall(pattrn, l)
        if ur:
            print(ur)
            if ur[0][1] not in res:
                res.append(ur[0][1])
res1 = sorted(res)
print('\n'.join(res1))
