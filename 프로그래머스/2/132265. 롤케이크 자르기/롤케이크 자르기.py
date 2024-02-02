from collections import Counter
def solution(toppings):
    answer =0
    older = Counter(toppings)
    younger=set()
    for topping in toppings:
        older[topping] -=1
        younger.add(topping)
        if older[topping] <=0:
            del older[topping]
        if len(older) == len(younger):
            answer +=1
    return answer