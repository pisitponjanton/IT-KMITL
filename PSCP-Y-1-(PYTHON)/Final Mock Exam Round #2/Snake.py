"""Snake"""
import json
def main(n):
    """Snake"""
    d={3:21,8:30,28:84,58:77,75:86,80:100,90:91,
       97:79,95:51,88:18,62:22,57:40,52:29,17:13}
    l=[[i,1] for i in range(1,n+1)]
    l1,s=[],0
    num = json.loads(input())
    for i in num:
        if s>=len(l[:]):
            s=0
        l[s][1]+=i
        if l[s][1] in d:
            l[s][1]=d[l[s][1]]
        if l[s][1]>=100 and l[s][0] not in l1:
            l1.append(l[s][0])
            l.pop(s)
            if len(l1)==n:
                break
        else:
            s+=1
    l.sort(key=lambda x:(-x[1],-x[0]))
    if l1:
        print(*l1)
    else:
        print(-1)
    if l:
        print(*[i[0] for i in l])
main(int(input()))
