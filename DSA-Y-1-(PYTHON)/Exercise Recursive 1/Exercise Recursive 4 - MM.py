"""Exercise Recursive 4 - MM"""
def mm(l):
    """MM"""
    n = input()
    if n != "End":
        l.append(int(n))
        mm(l)
    return l
def main(n,l=[]):
    """main"""
    if n != "End":
        l.append(int(n))
        mm(l)
    print(f"Max: {max(l)}\nMin: {min(l)}")
main(input())