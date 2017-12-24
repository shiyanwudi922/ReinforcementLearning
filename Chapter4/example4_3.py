#encoding=utf-8

import copy
import matplotlib.pyplot as plt

target = 100
value = [0.0]*(target + 1)
policy = [0]*(target + 1)
# for state in range(1, target):
#     max_stake = min(state, target-state)
#     policy[state] = [1.0/(max_stake+1)]*(max_stake+1)
reward = [0]*(target + 1)
reward[target] = 1.0

ph = 0.4

threshold = 0.00001
# delta = 100
delta_min = 10
max_iter = 10000
iter_cnt = 0
# while((delta > threshold or delta_min > threshold/10.0) and iter < max_iter):
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
    # print(delta)
print(value)
print(policy)
# for state in policy:
#     for action in range(len(policy[state])):
#         action_value = ph*(reward[state+action]+value[state+action]) + (1.0-ph)*(reward[state-action]+value[state-action])
#         policy[state][action] = action_value
#
#
#     # for action in range(len(policy[state])):
#     max_action = 1
#     max_action_value = policy[state][max_action]
#     for action in range(1, len(policy[state])):
#         if(policy[state][action] > max_action_value + threshold):
#             max_action_value = policy[state][action]
#             max_action = action
#
#     for action in range(len(policy[state])):
#         if(action == max_action):
#             policy[state][action] = 1
#         else:
#             policy[state][action] = 0


    # max_action_value = max(policy[state])
    # for action in range(len(policy[state])):
    #     if(max_action_value == policy[state][action]):
    #         policy[state][action] = 1
    #     else:
    #         policy[state][action] = 0

    # print("state: " + str(state))
    # print("    ".join([str(act) + ":" + str(val) for act, val in enumerate(policy[state])]))

    # action_value_sum = sum(policy[state])
    # for action in range(len(policy[state])):
    #     policy[state][action] /= action_value_sum

# print(value)

# for state in policy:
#     print("state: " + str(state))
#     print("    ".join([str(action) + ":" + str(pro) for action, pro in enumerate(policy[state])]))


