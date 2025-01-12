"""Supercar Parking"""
def main(n,s):
    """Supercar Parking"""
    for j,_ in enumerate(n):
        l1, l=1 if j>0 else 0, 1 if j<len(n)-1 else 0
        if n[j]=="0" and n[j+l]=="0" and n[j-l1]=="0":
            n[j]="1"
            s+=1
    print(s)
main(list(input()),0)
