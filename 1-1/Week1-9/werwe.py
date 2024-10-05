"""r"""
def main():
    """r"""
    a = int(input())
    b = int(input())
    goal = int(input())
    if goal < b*5:
        n =  b*5 - goal
        if n <= 5 :
            b -= 1
        else:
            b -= (n//5)+1
    goal = goal - b*5
    if goal <= a:
        print(goal)
    else:
        print(-1)
main()
