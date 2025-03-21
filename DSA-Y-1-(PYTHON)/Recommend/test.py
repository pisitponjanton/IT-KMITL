"""test"""
l1 = [33,30,31,35,36]
l2 = [400,365,360,410,422]
def main():
    """test"""
    s = 0
    for i in range(5):
        s+= ((l1[i]-33)/2.5495)*((l2[i]-391.4)/27.5645)
    print(s/4)
def xy():
    """xy"""
    s=0
    for i in range(5):
       s+= (l1[i]-33)*(l2[i]-391.4)
    print(s)
xy()