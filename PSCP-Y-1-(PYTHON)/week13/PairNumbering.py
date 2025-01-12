"""PairNumbering"""
import json
def main():
    """PairNumbering"""
    l1,l2,p,s=json.loads(input()),json.loads(input()),int(input()),0
    for i in l1:
        if i<=p:
            s+=list(l2).count(p-i)
    print(s)
main()
