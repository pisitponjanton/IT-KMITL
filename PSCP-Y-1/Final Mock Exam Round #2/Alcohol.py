"""Alcohol"""
def main():
    """Alcohol"""
    p = input()
    m = float(input())
    yn = input()
    cc = float(input())
    d = float(input())
    n = int(input())
    h = int(input())
    num = (d*cc*n)/100
    if p == "Male":
        num = num/(m*0.68*10)
    else:
        num = num/(m*0.55*10)
    num *= 1000
    num-=15*h
    if num<=50 and yn =="Yes":
        print("Safe")
    else:
        print("Not Safe")
main()
