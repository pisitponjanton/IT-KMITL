"""BishopMove"""
def pc(x,pa,yn):
    """rfr"""
    s = "No"
    for i in x:
        if pa[1] == i == pa[0] and yn:
            s = "Yes"
            break
        if pa[1] == i:
            s = "No"
            break
        if pa[0] == i:
            s = "Yes"
            break
    return s
def main(x,y,bx,by,ax,ay,yn,px,py):
    """BishopMove"""
    bxy,tr,br,tl,bl,pa = [bx,by],[],[],[],[],\
    [str(px)+" "+str(py),str(ax)+" "+str(ay)]
    while True:
        if not bxy[0] or not bxy[1]:
            break
        bxy[0]-=1
        bxy[1]-=1
        tr.append(f"{bxy[0]} {bxy[1]}")
    bxy[0],bxy[1]=bx,by
    while True:
        if not bxy[0] or bxy[1]==y:
            break
        bxy[0]-=1
        bxy[1]+=1
        tl.append(f"{bxy[0]} {bxy[1]}")
    bxy[0],bxy[1]=bx,by
    while True:
        if bxy[0]==x or not bxy[1]:
            break
        bxy[0]+=1
        bxy[1]-=1
        br.append(f"{bxy[0]} {bxy[1]}")
    bxy[0],bxy[1]=bx,by
    while True:
        if bxy[0]==x or bxy[1]==y:
            break
        bxy[0]+=1
        bxy[1]+=1
        bl.append(f"{bxy[0]} {bxy[1]}")
    x="Yes" if bx == px and by==py else "No"
    if pa[0] in tr:
        x = pc(tr,pa,yn)
    elif pa[0] in tl:
        x = pc(tl,pa,yn)
    elif pa[0] in br:
        x = pc(br,pa,yn)
    elif pa[0] in bl:
        x = pc(bl,pa,yn)
    print(x)
main(int(input()),int(input()),int(input()),
     int(input()),int(input()),int(input()),
     int(input()),int(input()),int(input()))
