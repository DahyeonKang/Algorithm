import queue  # 파이썬에서 queue 모듈은 큐와 스택 클래스를 제공한다.

Q = queue.Queue(maxsize=20)  # 큐 객체 생성, 최대크기는 20

print(Q.empty(), Q.full())  # 큐 상태 확인하기
for v in range(1, 10):  # 큐에 1-10 넣기
    Q.put(v)  # put()로 큐 안에 값 넣기

print(Q.empty())  # get() 수행 전 공백상태 아닌지 확인
print("큐의 내용: ", end='')
for _ in range(1, 10):
    print(Q.get(), end=' ')  # get()로 큐 안의 데이터 삭제

# 공백상태의 큐에 get() 연산을 수행하면 Underflow 발생
# maxsize 이상의 항목을 put()하는 경우 Overflow 발생
