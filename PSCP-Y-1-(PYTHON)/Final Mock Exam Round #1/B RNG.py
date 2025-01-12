"""[Mock Final 2022] B RNG"""
import json
def max_sum_from_list(lst, n, s):
    """[Mock Final 2022] B RNG"""
    max_sum = 0
    length = len(lst)
    for i in range(length):
        current_sum = 0
        visited = set()
        position = i
        for j in range(n):
            if position in visited:
                break
            visited.add(position)
            current_sum += lst[position]
            position = (position + s) % length
        max_sum = max(max_sum, current_sum)
    return max_sum
lst = json.loads(input())
n = int(input())
s = int(input())
result = max_sum_from_list(lst, n, s)
print(result)
