"""[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main(n):
    """[Final 2021] เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
    d = {"BULL SHARK":"THE SHALLOW ZONE",
         "BLUE SHARK":"THE TWILIGHT ZONE",
         "GREAT WHITE SHARK":"THE TWILIGHT ZONE",
         "GUMMY SHARK":"THE TWILIGHT ZONE",
         "MAKO SHARK":"THE TWILIGHT ZONE",
         "FRILLED SHARK":"THE MIDNIGHT ZONE",
         "GOBLIN SHARK":"THE MIDNIGHT ZONE",
         "SIXGILL SHARK":"THE MIDNIGHT ZONE",
         "GREENLAND SHARK":"THE MIDNIGHT ZONE",
         "COOKIECUTTER SHARK":"THE MIDNIGHT ZONE",
         "MEGAMOUTH SHARK":"THE ABYSSAL ZONE",
         "CHAIN CATSHARK":"THE TWILIGHT ZONE",
    }
    if "SHARK" in n:
        print(d[n])
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main(input())
