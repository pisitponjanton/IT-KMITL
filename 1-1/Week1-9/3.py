def main(n):
    s=0
    for i in range(1,int(n**0.5)+1):
        if not n%i:
            s+=i
            print(i)
            if i>1:
                s+=n//i
                print(n//i)
    print(s)
main(int(input()))