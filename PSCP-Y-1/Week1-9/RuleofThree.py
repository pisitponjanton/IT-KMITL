"""RuleofThree"""
def main():
    """RuleofThree"""
    num = int(input())
    num1list = []
    num2list = []
    num3list = []
    for _ in range(1,num+1):
        num1 = float(input())
        num2 = float(input())
        num1list.append(num1)
        num2list.append(num2)
        num3list.append(num2/num1)
    n = []
    for i in range(len(num3list)):
        if num3list[i] == max(num3list):
            n.append(i)
    l = []
    for i in range(len(n)):
        l.append(num1list[n[i]])
    index = num1list.index(min(l))
    print(f"{num1list[index]:.2f} {num2list[index]:.2f}")
main()
