"""Labs 07.02 - Selection Sort"""
import json
def main(l,x):
    """Labs 07.02 - Selection Sort"""
    count=0
    for i in range(x):
        s=i
        for j in range(i+1,x+1):
            if l[j] <= l[i] and l[j] <= l[s]:
                s = j
            count+=1
        l[i],l[s]= l[s],l[i]
        print(l)
    print("Comparison times:",count)
main(json.loads(input()),int(input()))