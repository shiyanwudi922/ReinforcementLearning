#encoding=utf-8

import copy
import matplotlib.pyplot as plt

target = 100
value = [0.0]*(target + 1)
policy = [0]*(target + 1)
reward = [0]*(target + 1)
reward[target] = 1.0

ph = 0.4

threshold = 0.00001
delta_min = 10
max_iter = 10000
iter_cnt = 0

while True:
    iter_cnt += 1
    print("iteration cnt: " + str(iter))
    delta_list = []
    for i in range(1, target):
        old_value = value[i]
        for j in range(1, min(i+1, target+1-i)):
            action_value = ph * (reward[i + j] + value[i + j]) + (1.0 - ph) * (reward[i - j] + value[i - j])
            if(action_value > value[i] + threshold):
                value[i] = action_value
                policy[i] = j
        delta_list.append(abs(value[i]-old_value))
    delta = max(delta_list)
    if(delta < threshold or iter_cnt > max_iter):
        break

print(value)
print(policy)



