"""Parallelogram"""
def main():
    """Parallelogram"""
    n = input()
    for i in range(1,len(n)+1):
        print(f"{n[0:i]:>{len(n)}}")
    for i in range(1,len(n)):
        print(f"{n[i:]:<{len(n)}}")
main()
