from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    current_weight = deque()
    current_location = deque()
    t = 0
    while truck_weights or current_weight:
        t += 1
        if truck_weights:
            if (weight - sum(current_weight)) >= truck_weights[0]:
                current_weight.append(truck_weights.popleft())
                current_location.append(0)
        
        for i in range(len(current_location)):
            current_location[i] += 1
        
        if current_location[0] == bridge_length:
            current_weight.popleft()
            current_location.popleft()
    
    return t+1