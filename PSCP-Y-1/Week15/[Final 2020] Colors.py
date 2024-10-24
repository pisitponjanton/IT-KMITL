"""[Final 2020] Colors"""
def main(c1,c2):
    """[Final 2020] Colors"""
    d={"RedYellow":"Orange",
       "RedRed":"Red",
       "YellowRed":"Orange",
       "RedBlue":"Violet",
       "BlueBlue":"Blue",
       "BlueRed":"Violet",
       "YellowBlue":"Green",
       "YellowYellow":"Yellow",
       "BlueYellow":"Green"}
    c=c1+c2
    print(d[c] if c in d else "Error")
main(input(),input())
