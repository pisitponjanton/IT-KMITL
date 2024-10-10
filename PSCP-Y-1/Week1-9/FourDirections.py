"""FourDirections"""
def main():
    """FourDirections"""
    l = ["  *  "," *   ","*****"," *   ","  *  "]
    r = ["  *  ","   * ","*****","   * ","  *  "]
    d = ["  *  ","  *  ","* * *"," *** ","  *  "]
    u = ["  *  "," *** ","* * *","  *  ","  *  "]
    t = input()
    y = {'L': l, 'R': r, 'D': d, 'U': u}
    for i in range(5):
        p = ""
        for j in t:
            p+= y[j][i] + " "
        print(p)
main()
