s = input().split('-')
adder = []
for i in s:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    adder.append(cnt)

result = adder[0]
for i in adder[1:]:
    result -= i
print(result)
    
