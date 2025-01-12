"""[Final 2020] Resistor"""
def main(n1,n2,n3,n4):
    """[Final 2020] Resistor"""
    d = {"Black": 0,"Brown": 1,"Red": 2,
    "Orange": 3,"Yellow": 4,"Green": 5,
    "Blue": 6,"Purple": 7,"Grey": 8,"White": 9}
    c1 = {"Black": 1,"Brown": 10,"Red": 100,
    "Orange": 1000,"Yellow": 10000,"Green": 100000,
    "Blue": 1000000,"Purple": 10000000,"Gold": 0.1,"Silver": 0.01}
    c2 = {"Brown": 1,"Red": 2,"Green": 0.5,
    "Blue": 0.25,"Purple": 0.1,"Grey": 0.05,"Gold": 5,"Silver": 10}
    if n1 in d and n2 in d and n3 in c1 and n4 in c2:
        n=int(str(d[n1])+str(d[n2]))*c1[n3]
        print(f"{n*(100-c2[n4])/100:.4f}\n{n*(100+c2[n4])/100:.4f}")
    else:
        print("Error")
main(input(),input(),input(),input())
