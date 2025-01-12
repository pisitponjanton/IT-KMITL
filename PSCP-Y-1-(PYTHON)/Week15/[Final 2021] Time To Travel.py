"""[Final 2021] Time To Travel"""
def main(num):
    """[Final 2021] Time To Travel"""
    d1={0:"Start",1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'Stop',
        8:"G",9:"H",10:"I",11:"J",12:"K",13:"L",14:"Landmark x 2",15:"M",
        16:"N",17:"O",18:"P",19:"Q",20:"R",21:"Travel",22:"S",23:"T",24:"U",
        25:"V",26:"W",27:"X"}
    d2 = {'A': 1000, 'B': 1100, 'C': 1200, 'D': 1300, 'E': 1400, 'F': 1500,
    'G': 1600, 'H': 1700, 'I': 1800, 'J': 1900, 'K': 2000, 'L': 2100, 'M': 2200,
    'N': 2300, 'O': 2400, 'P': 2500, 'Q': 2600, 'R': 2700, 'S': 2800, 'T': 2900, 
    'U': 3000, 'V': 3100, 'W': 3200, 'X': 3300}
    s1,s2=num,num
    n1,n2=0,0
    st=0
    for i in range(int(input())):
        if st1:
            sto1=input()
            st1=0
            if "pay" in sto1:
                s1-=s1%10//100 
            else:
                pass
        n = input().split()
        if (i+1)%2: #p1
            n1+=int(n[1])+int(n[2])
            if n1>=28:
                n1-=28
            p=d1[n1]
            if p=="Start":
                s1+=num//2
            elif p=="Stop":
                st1=1
main(int(input()))
