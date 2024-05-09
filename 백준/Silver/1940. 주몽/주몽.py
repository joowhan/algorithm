# 2개의 재료로 옷을 만들고 m이 되면 만들여진다.
# n개의 재료, m, 몇개의 갑옷을 만들 수 있을지?


import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
count = 0

arr = list(map(int, input().split()))
arr.sort()
start = 0
end = len(arr)-1

while start < end:
    temp = arr[start]+arr[end]
    if temp == m:
        count +=1
        end -=1
    elif temp < m:
        start +=1
    else:
        end -=1

print(count)