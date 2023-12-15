self_number = [i for i in range(1, 10001)]
for i in range(1, 10001):
    temp = i
    n = str(i)
    for j in range(len(n)):
        temp += int(n[j])
    if temp in self_number:
        self_number.remove(temp)
for num in self_number:
    print(num)