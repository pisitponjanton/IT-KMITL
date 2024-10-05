"""[Final 2019] IP Address"""
def main(n,t=0,l="",s=0):
    """[Final 2019] IP Address"""
    if str(n).count(".")==3:
        m = str(n).split(".")
        for i in m:
            for j in i:
                if not j.isnumeric():
                    t=1
                    break
        if not t:
            for i in m:
                if int(i)>255 or int(i)<0:
                    t=1
                    break
            for i in m:
                l+=str(int(i))
                if s!=len(m)-1:
                    l+="."
                s+=1
        print("Invalid IPv4 address" if t else l)
    else:
        print("Invalid IPv4 address")
main(input())
