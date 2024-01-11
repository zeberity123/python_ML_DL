import json
# load: 문자열 -> 객체
# dump: 객체 -> 문자열

j = '{"ip": "8.8.8.8"}'
d = json.loads(j)

s = str(d)
print(s, type(s))

dt = '''{
    "time": "03:53:25 AM",
    "milliseconds_since_epoch": 1362196405309,
    "date": "03-02-2013"
}'''

dl = json.loads(dt)
# print(dl['time'])
for k in dl:
    print(k, dl[k])

print(dl.keys())
print(dl.values())
print(dl['time'], dl['milliseconds_since_epoch'], dl['date'])
