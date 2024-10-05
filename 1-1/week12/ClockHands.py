"""ClockHands"""
def main(h,m):
    """ClockHands"""
    print("True" if h*30+m*0.5-m*6>=0 and abs(h*30+m*0.5-m*6)<=6 else "False")
main(int(input()),int(input()))
