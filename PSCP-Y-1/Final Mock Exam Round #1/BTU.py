"""BTU"""
def mm1(x):
    """efw"""
    btu=0
    if 451 <=x<= 550:
        btu = 12000
    elif 551 <=x<= 700:
        btu = 14000
    elif 701 <=x<= 1000:
        btu = 18000
    elif 1001 <=x<= 1200:
        btu = 21000
    elif 1201 <=x<= 1400:
        btu = 23000
    elif 1401 <=x<= 1500:
        btu = 24000
    elif 1501 <=x<= 2000:
        btu = 30000
    elif 2001 <=x<= 2500:
        btu = 34000
    return btu
def mm(x):
    """1050"""
    if 100 <=x<= 150:
        btu = 5000
    elif 151 <=x<= 250:
        btu = 6000
    elif 251 <=x<= 300:
        btu = 7000
    elif 301 <=x<= 350:
        btu = 8000
    elif 351 <=x<= 400:
        btu = 9000
    elif 401 <=x<= 450:
        btu = 10000
    else:
        btu = mm1(x)
    return btu
def main(x,h,n,l1,l2):
    """BTU"""
    b = mm(x)
    if h>8:
        b+=1000*(h-8)
    if n>2:
        b+=600*(n-2)
    if l1!="Normal":
        b+=4000
    if l2=="facing the sun":
        b+=10*b//100
    elif l2 == "shaded":
        b-=10*b//100
    print(b)
main(int(input()),int(input()),int(input()),input(),input())
