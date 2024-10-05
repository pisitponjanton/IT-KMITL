"""Digit v2"""
def main(n):
    """Digit v2"""
    s=0
    if "hundred thousand" in n:
        s+=6
    elif "ten thousand" in n or "ty thousand" in n or "teen thousand" in n \
    or "eleven thousand" in n or "twelve thousand" in n:
        s+=5
    elif "thousand" in n:
        s+=4
    elif "hundred" in n:
        s+=3
    elif "ty" in n or "ten" in n or "teen" in n or "eleven" in n or "twelve" in n:
        s+=2
    else:
        s+=1
    print(s)
main(input())
