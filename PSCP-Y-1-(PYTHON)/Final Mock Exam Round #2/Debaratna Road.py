"""Debaratna Road"""
def main(x):
    """Debaratna Road"""
    if 0<=x<=5.032:
        print("Bangkok")
    elif 5.032<x<=35.477:
        print("Samut Prakarn")
    elif 35.477<x<=52.9:
        print("Chachoengsao")
    elif 52.9<x<=58.855:
        print("Chon Buri")
    else:
        print("InValid")
main(float(input()))
