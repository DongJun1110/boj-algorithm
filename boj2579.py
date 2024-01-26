stairs = [0]*301
n=int(input())
for i in range(n):
  stairs[i]=int(input())

op=[0]*301
op[0]=stairs[0]
op[1]=stairs[0]+stairs[1]
op[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,n):
  op[i]=max(op[i-3]+stairs[i-1]+stairs[i], op[i-2]+stairs[i])

print(op[n-1])