'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
* 프로그램명 : dict_search.py
* 작성일 : 2021.11.03.Wed
* 프로그램 설명 : 파이썬의 딕셔너리를 이용한 맵의 결과 구현하기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


d = {}
d['data'] = '자료'
d['structure'] = '구조'
d['sequential search'] = '선형 탐색'
d['game'] = '게임'
d['binary search'] = '이진 탐색'
print("나의 단어장")
print(d)

if d.get('game'):
    print('탐색:game --> ', d['game'])
if d.get('over'):
    print('탐색:over --> ', d['over'])
if d.get('data'):
    print('탐색:data --> ', d['data'])

d.pop('game')
print('나의 단어장:')
print(d)