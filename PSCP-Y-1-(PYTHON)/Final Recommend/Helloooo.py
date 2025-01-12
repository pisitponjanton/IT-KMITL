"""Helloooo"""
def main(n,s='',e=0):
    """Helloooo"""
    for i in n[::-1]:
        if i.lower() in "aeiou" and not e:
            s+=i*4
            e=1
        else:
            s+=i
    print(s[::-1])
main(input())
