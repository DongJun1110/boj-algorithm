t = int(input())
for _ in range(t):
  words = input().split()
  for i in range(len(words)):
    word = words[i]
    print(word[::-1],end=' ')