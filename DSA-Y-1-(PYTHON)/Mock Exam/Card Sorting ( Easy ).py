"""Card Sorting ( Easy )"""
import json

def sod(x):
    d = {"A" : 1,"K" : 13,"Q" : 12,"J" : 11}
    if x[0] in d:
        return -ord(x[-1]),-d[x[0]]
    return -ord(x[-1]),-int(x[:-1])

def s_2(l,key):
    while True:
        swapped = False
        for i in range(1, len(l)):
            if key(l[i]) < key(l[i - 1]):
                l[i], l[i - 1] = l[i - 1], l[i]
                swapped = True
        if not swapped:
            break
    return l
def s_3(x):
    return -x[2], tuple(-ord(c) for c in x[0])
def main(x,_):
    """Card Sorting ( Easy )"""
    l = []
    for _ in range(x):
        inp = json.loads(input())
        inp[1] = s_2(inp[1],sod)
        sum = 0
        for i in inp[1]:
            if i in ("2C","QS"):
                sum+=50
            elif "A" in i:
                sum+=15
            elif "10" in i or i[0] in ("K","Q","J"):
                sum+=10
            else:
                sum+=5
        l.append(inp+[sum])
    l = s_2(l,s_3)
    for i in l:
        print(f"{i[0]} -> {i[2]} -> {i[1]}")
main(int(input()),int(input()))
