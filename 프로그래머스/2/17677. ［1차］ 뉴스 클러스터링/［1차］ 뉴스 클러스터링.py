def solution(str1, str2):
    str1, str2 = str1.upper() , str2.upper()
    m = max(len(str1), len(str2))
    list1, list2 = [], []

    for x in range(0,m):
        if x+2 <= len(str1) and str1[x:x+2].isalpha():
            list1.append(str1[x:x+2])
        if x+2 <= len(str2) and str2[x:x+2].isalpha():
            list2.append(str2[x:x+2])
    print(list1, list2)
    if len(list1) + len(list2) == 0:
        return 65536

    cnt = 0

    temp = list1[:]
    for k in temp:
        if k in list2:
            list2.remove(k)
            cnt += 1

    return int(65536*cnt/(len(list1) + len(list2)))