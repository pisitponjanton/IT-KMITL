"""Lab 01.02 - Max…Min…Avg"""
import json
def m1(x):
    """Lab 01.02 - Max…Min…Avg"""
    r=x[0]
    for i in x:
        if i<r:
            r=i
    return r
def m2(x):
    """Lab 01.02 - Max…Min…Avg"""
    r=x[0]
    for i in x:
        if i>r:
            r=i
    return r
def main(x):
    """Lab 01.02 - Max…Min…Avg"""
    avg = sum(x)/len(x)
    print((m2(x),m1(x),round(avg, 2)))
main(json.loads(input()))
