n = int(input())
result = 0
arr = []
for x in range(n):
  for y in range(n):
    if x*5 + y*3 == n:
      arr.append(x+y)

try:
  arr.sort()
  print(arr.pop(0))
except:
  print(-1)