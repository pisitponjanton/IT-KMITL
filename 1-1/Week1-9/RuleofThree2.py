"""RuleofThree"""
def main():
    """RuleofThree"""
    num = int(input())
    num1list = []
    num2list = []
    num3list = []
    for _ in range(num):
        num1 = float(input())
        num2 = float(input())
        num1list.append(num1)
        num2list.append(num2)
        num3list.append(num2 / num1)
    max_index = num3list.index(max(num3list))
    max_vnum1list = [num1list[i] for i, val in enumerate(num3list) if val == num3list[max_index]]
    min_vindex = num1list.index(min(max_vnum1list))
    print(f"{num1list[min_vindex]:.2f} {num2list[min_vindex]:.2f}")
main()
