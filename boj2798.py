n,m = map(int,input().split())
li = list(map(int,input().split()))
sum = []
for i in range(n):
  for k in range(i+1,n):
    for j in range(k+1,n):
      if (li[i]+li[k]+li[j])<=m:
        sum.append(li[i]+li[k]+li[j])
      
sum.sort(reverse = True)
print(sum[0])

  