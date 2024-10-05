"""Filter"""
def main():
    """Filter"""
    n=input().replace("{","").replace("}","").replace("\"","")
    num = float(input())
    n=n.split(", ")
    l = []
    for i in n:
        l.append(i.split(": "))
    l.sort(key=lambda x: x[0][:])
    for i in l[:]:
        if float(i[1])<num:
            l.remove(i)
    if l:
        for i in l:
            print(f"{i[0]}\t{float(i[1]):.2f}")
    else:
        print("Nope")
main()
