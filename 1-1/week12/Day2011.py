"""Day2011"""
def main():
    """Day2011"""
    d = int(input())
    m = int(input())
    if m < 3:
        m += 12
        year = 2010
    else:
        year = 2011
    k = year % 100
    j = year // 100
    f = d + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    day = f % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(days[day])
main()
