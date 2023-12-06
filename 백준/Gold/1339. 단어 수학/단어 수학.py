n = int(input())
words={}
for _ in range(n):
    word = input().rstrip()
    for j in range(len(word)):
        words[word[j]] = words.get(word[j], 0) + 10**(len(word)-j-1)
temp = sorted(words.items(), key=lambda x:x[1], reverse=True)
num = 9
answer = 0
for word in temp:
    answer += num*word[1]
    num -=1
print(answer)