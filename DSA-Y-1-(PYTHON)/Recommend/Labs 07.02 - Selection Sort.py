"""Labs 07.02 - Selection Sort"""
import json
def main(l,end):
    """Labs 07.02 - Selection Sort"""
    n = 0
    for i in range(end):
        min = i
        for j in range(i+1,end+1):
            if l[j] < l[min]:
                min = j
            n+=1
        l[i],l[min] = l[min],l[i]
        print(l)
    print("Comparison times:",n)
main(json.loads(input()),int(input()))
