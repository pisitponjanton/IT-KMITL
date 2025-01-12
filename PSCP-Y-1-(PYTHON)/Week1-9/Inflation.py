"""Inflation"""
def main():
    """Inflation"""
    num1 = int(float(input()) * 100)
    num2 = int(input())
    s = 381
    for _ in range(num2):
        num1 += (num1 * s) // 10000
    print(f"{num1//100}.{num1 % 100:02d}")
main()
