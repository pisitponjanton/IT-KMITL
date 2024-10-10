"""Backward"""
def main():
    """Backward"""
    n=0
    t=[]
    while not n:
        text = input()
        if text == "NULL":
            break
        t.append(text)
    for i in t[::-1]:
        print(i)
main()
