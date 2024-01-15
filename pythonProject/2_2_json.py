# 2_2_json.py
import json

# load: 문자열 -> 객체 : 상대방으로부터 수신
# dump: 객체 -> 문자열 : 상대방에게 송신

j = '{"ip": "8.8.8.8"}'
d = json.loads(j)
print(d, type(d))

# 퀴즈
# 딕셔너리를 json 문자열로 변환하세요
s = json.dumps(d)
print(s, type(s))

# 아래 데이터로부터 값에 해당하는 것만 출력하세요
dt = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

d2 = json.loads(dt)
print(d2)

for k in d2:
    print(k, d2[k])

print(d2.keys())
print(d2.values())
print(d2['time'], d2['milliseconds_since_epoch'], d2['date'])


