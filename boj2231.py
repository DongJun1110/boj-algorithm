n = int(input())

for i in range(1,n+1):
  if (sum(list(map(int,str(i)))) + i) == n:
    print(i)
    break
  if i == n:
    print(0)
  