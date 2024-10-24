"""TicTacToe"""
def main(s=""):
    """TicTacToe"""
    for _ in range(3):
        s+=input().replace('O','1').replace('X','0')
    l1=[[s[0],s[1],s[2]],[s[3],s[4],s[5]],[s[6],s[7],s[8]],
        [s[0],s[3],s[6]],[s[1],s[4],s[7]],[s[2],s[5],s[8]],
        [s[0],s[4],s[8]],[s[2],s[4],s[6]]]
    x = all(i == "1" for i in l1[0]) or all(i=="1" for i in l1[1])\
    or all(i=="1" for i in l1[2]) or all(i=="1" for i in l1[7])
    x1 = all(i=="1"for i in l1[3]) or all(i=="1"for i in l1[4])\
    or all(i=="1"for i in l1[5]) or all(i=="1" for i in l1[6])
    y = all(i == "0" for i in l1[0]) or all(i=="0" for i in l1[1])\
    or all(i=="0" for i in l1[2]) or all(i=="0" for i in l1[7])
    y1 = all(i=="0"for i in l1[3]) or all(i=="0"for i in l1[4])\
    or all(i=="0"for i in l1[5]) or all(i=="0" for i in l1[6])
    print("O WIN" if x or x1 else "X WIN" if y or y1 else "DRAW")
main()
