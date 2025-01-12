"""Nearer"""
def nearer():
    """Nearer"""
    a = int(input())
    b = int(input())
    c = int(input())
    ca = abs(c-a)
    cb = abs(c-b)
    if ca < cb:
        print(f"Alice {ca}")
    elif ca > cb:
        print(f"Bob {cb}")
    else:
        print(f"Sundaes {cb}")
nearer()
