import sys

q = []

for _ in range(int(sys.stdin.readline())):
  command = list(sys.stdin.readline().split())

  if command[0] == 'push':
    q.append(command[1])

  elif command[0] == 'pop':
    if q:
      print(q.pop(0))
    else:
      print(-1)

  elif command[0] == 'size':
    print(len(q))

  elif command[0] == 'empty':
    if len(q) == 0:
      print(1)
    else:
      print(0)

  elif command[0] == 'back':
    if q:
      print(q[len(q)-1])
    else:
      print(-1)

  elif command[0] == 'front':
    if q:
      print(q[0])
    else:
      print(-1)

