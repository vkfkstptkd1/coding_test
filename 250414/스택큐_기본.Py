#스택_기본.Py

stack=[]
stack.append(5)
stack.append(6)
stack.append(8)
stack.pop()
stack.append(7)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

from collections import deque

queue =deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)