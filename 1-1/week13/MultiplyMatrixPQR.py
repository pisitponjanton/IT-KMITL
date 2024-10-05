"""MultiplyMatrixPQR"""
def main(p,q,r):
    """MultiplyMatrixPQR"""
    a,b=[],[]
    for _ in range(p):
        a.append([int(input()) for _ in range(q)])
    for _ in range(q):
        b.append([int(input()) for _ in range(r)])
    result = [[0 for _ in range(r)] for _ in range(p)]
    for i in range(p):
        for j in range(r):
            for k in range(q):
                result[i][j] += a[i][k] * b[k][j]
    for row in result:
        print(' '.join(map(str, row)))
main(int(input()),int(input()),int(input()))
