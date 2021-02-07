# 스택과 큐

스택과 큐는 삽입, 삭제 연산과 오버플로우, 언더플로우 개념이 중요하다.

* 삽입: 데이터를 삽입
* 삭제: 데이터를 삭제
* 오버플로우: 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
* 언더플로우: 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생

## 스택

* 선입후출(First In Last Out) 또는 후입선출 구조
* list 사용
* 삽입연산 -> append 함수
* 삭제연산 -> pop 함수

~~~
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  ## [5,2,3,1]
print(stack[::-1])  ## [1,3,2,5]
~~~

## 큐

* 선입선출(First In First Out)구조 
* collection 모듈의 deque 사용
* 삽입연산 -> append()
* 삭제연산 -> popleft()
~~~
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  ## dequeue([3,7,1,4])
queue.reverse()  ## 역순으로 바꾼다.   
print(queue)  ## dequeue([4,1,7,3])
list(queue)  ## 리스트로 바꾼다. 
~~~