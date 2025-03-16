"""Shadow&Dragon"""
def main():
    """Shadow&Dragon"""
    _ = input()
    at_p = input().split()
    at_p = [int(i) for i in at_p]
    de_p = input().split()
    de_p = sum([int(i) for i in de_p])
    y = int(input())
    at_d = input().split()
    at_d = [int(i) for i in at_d]
    de_d = input().split()
    de_d = [int(i) for i in de_d]
    for i in range(y):
        num = 0
        if at_d[i] > de_p:
            num += (at_d[i] - de_p) +1
        if de_d[i] > max(at_p):
            num += de_d[i] - max(at_p)
        print(num)
main()
