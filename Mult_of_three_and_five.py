import math
'''
new_list = range(0, 1001)

for i in list(new_list):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
'''

print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))



