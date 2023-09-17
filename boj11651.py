n = int(input())
arr = []
for i in range(n):
  point = list(map(int,input().split()))
  arr.append(point)

arr.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
  print(arr[i][0], arr[i][1])