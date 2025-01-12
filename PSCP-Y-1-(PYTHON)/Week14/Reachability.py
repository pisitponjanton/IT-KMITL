"""Reachability"""
import json
def main(d,v):
    """Reachability"""
    l = [d[i] for i in d[v]]
    l = [j for i in l for j in i]
    for _ in range(40):
        l = [d[i] for i in l]
        l = [j for i in l for j in i]+[v]
        l = list(set(l))
    l.sort()
    print(l)
main(json.loads(input().replace("'","\"")),input())
