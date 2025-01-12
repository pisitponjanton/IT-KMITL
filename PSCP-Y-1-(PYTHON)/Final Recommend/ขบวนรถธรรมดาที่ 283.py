"""ขบวนรถธรรมดาที่ 283"""
def main(n):
    """ขบวนรถธรรมดาที่ 283"""
    s2,s1,num2,num1=0,0,0,0
    while True:
        t=input().split(", ")
        if t[0]==n[0]:
            s1=1
            num2=float(t[1])
        if t[0]==n[1]:
            s2=1
            num1=float(t[1])
        if "Done" in t or s1+s2==2:
            break
    print(f"{abs(num1-num2):.2f}" if s1+s2==2 else "Error")
main(input().split(", "))
