T = int(input())

for tc in range(T):
  stack = []
  ip = input()
  
  for i in ip:
    if i == '(':
      stack.append(i)
    else:
      if len(stack) == 0:
        stack.append(i)
        break
      else:
        stack.pop()

  if len(stack) == 0:
    print('YES')
  else:
    print('NO')

  