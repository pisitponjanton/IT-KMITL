"""Supercar Parking"""
def main():
    """Supercar Parking"""
    parking = input().strip()
    parking = list(parking)
    count = 0
    n = len(parking)
    for i in range(n):
        if parking[i] == '0':
            left_empty = not i or parking[i - 1] == '0'
            right_empty = i == n - 1 or parking[i + 1] == '0'
            if left_empty and right_empty:
                parking[i] = '1'
                count += 1
    print(count)
main()
