"""Helloooo"""
def main(x):
    """Helloooo"""
    s,o='',0
    for i in x[::-1]:
        if i in ('a','e','i','o','u') and not o:
            s+=i*4
            o=1
        else:
            s+=i
    print(s[::-1])
main(input())
