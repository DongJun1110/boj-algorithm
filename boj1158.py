n,k = map(int,input().split())
li = [i+1 for i in range(n)]
result = []
idx = 0

for i in range(n):
  idx += k-1
  if idx >= len(li):
    idx = idx % len(li)
  result.append(li.pop(idx))

print('<',end='')
for i in result:
  if i == result[len(result)-1]:
    print(i,end='')
  else: print(i,',',sep='',end=' ')
print('>')
