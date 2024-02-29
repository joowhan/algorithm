from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    onbridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    crossing = 0
    while len(truck_weights):
        time += 1
        crossing -= onbridge.popleft()
        if crossing + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            crossing += truck
            onbridge.append(truck)
        else:
            onbridge.append(0)
    time += bridge_length
    return time