import sys
from collections import deque

dq = deque()

for _ in range(int(sys.stdin.readline())):
  command = list(sys.stdin.readline().split())
  if command[0] == 'push_front':
    dq.append(command[1])
    
  elif command[0] == 'push_back':
    dq.appendleft(command[1])
    
  elif command[0] == 'pop_front':
    if dq: print(dq.pop())
    else: print(-1)

  elif command[0] == 'pop_back':
    if dq: print(dq.popleft())
    else: print(-1)

  elif command[0] == 'size':
    print(len(dq))

  elif command[0] == 'empty':
    print(0) if len(dq) != 0 else print(1)

  elif command[0] == 'front':
    print(dq[len(dq)-1]) if len(dq) != 0 else print(-1)

  elif command[0] == 'back':
    print(dq[0]) if len(dq) != 0 else print(-1)

