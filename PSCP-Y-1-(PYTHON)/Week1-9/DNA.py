"""DNA"""
def main():
    """DNA"""
    n1 = input()
    n2 = input()
    s=0
    for i,j in zip(n1,n2):
        if not i in ("A","C","G","T"):
            s=1
        if not j in ("A","C","G","T"):
            s=1
    if not s:
        m,n=len(n1),len(n2)
        start=0
        end=0
        t=""
        for i in range(m):
            for j in range(n):
                r = 0
                while (i+r<m) and (j+r<n) and n1[i+r] == n2[j+r]:
                    r += 1
                if r > start:
                    start = r
                    end = i + r
        t = n1[end - start:end]
        print(t if t else "None")
    else:
        print("Error")
main()
