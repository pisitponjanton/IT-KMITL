import json
def main(x,y,z):
    """main"""
    x1 = [True for i in x if i in y and i in z]
    y1 = [True for i in y if i in x and i in z]
    z1 = [True for i in z if i in y and i in x]
    b = bool(x1 and y1 and z1)
    print(b)
main(json.loads(input()),json.loads(input()),json.loads(input()))