n, game = input().split()
n = int(n)
member = set()
for  i in range(n):
    member.add(input())
if game == 'Y':
    print(len(member))
elif game=='F':
    print(len(member)//2)
else:
    print(len(member)//3)    
