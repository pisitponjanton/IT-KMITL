"""[Final 2019] Mickey"""
def main(n):
    """[Final 2019] Mickey"""
    m,h = [int(input()) for _ in range(n)],[int(input()) for _ in range(n)]
    m.sort()
    h.sort()
    print(max((abs(i-j) for i,j in zip(m,h))))
main(int(input()))
