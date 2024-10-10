"""Inverter"""
def main(n):
    """Inverter"""
    print(int(str(n).translate({48:49,49:48})) if int(str(n).translate({48:49,49:48})) > 0 else "")
main(input())
