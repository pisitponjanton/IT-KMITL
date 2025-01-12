"""[Final 2021] DigitMatrix"""
import math
def main():
    """[Final 2021] DigitMatrix"""
    d={"******   **   **   ******":0,
       "    *    *    *    *    *":1,
       "*****    *******    *****":2,
       "*****    ******    ******":3,
       "*   **   ******    *    *":4,
       "******    *****    ******":5,
       "******    ******   ******":6,
       "*****    *    *    *    *":7,
       "******   *******   ******":8,
       "******   ******    ******":9,
       "  *    *  *****  *    *  ":"+",
       "          *****          ":"-",
       "*   * * *   *   * * *   *":"x",
       "  *       *****       *  ":"/",
       }
    l = [input() for _ in range(5)]
    l1=""
    l2=""
    l3=""
    for i in l:
        for j,z in enumerate(i):
            if j<5:
                l1+=z
            elif 7<=j<12:
                l2+=z
            elif j>=14:
                l3+=z
    if d[l2]=="+":
        print(d[l1]+d[l3])
    elif d[l2]=="-":
        print(d[l1]-d[l3])
    elif d[l2]=="x":
        print(d[l1]*d[l3])
    else:
        print(math.ceil(d[l1]/d[l3]) if d[l3] else "Error")
main()
