"""ขบวนรถธรรมดาที่ 283"""
def main(x,s1=0,s2=0):
    """ขบวนรถธรรมดาที่ 283"""
    s11,s22=0,0
    while True:
        num = input().split(", ")
        if "Done" in num:
            break
        if x[0] == num[0]:
            s1=float(num[1])
            s11=1
        if x[1] == num[0]:
            s2=float(num[1])
            s22=1
        if s22 and s11:
            break
    if s22 and s11:
        s=abs(s2-s1)
        print(f"{s:.2f}")
    else:
        print("Error")
main(input().split(", "))
