"""Divide3Or5"""
def main():
    """Divide3Or5"""
    s=0
    for i in range(2,int(input())+1):
        if not i%3 or not i%5:
            s+=i
    print(s)
main()
