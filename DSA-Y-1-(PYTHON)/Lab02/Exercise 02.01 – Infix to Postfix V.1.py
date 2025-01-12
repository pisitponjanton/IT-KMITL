"""Exercise 02.01 – Infix to Postfix V.1"""
class Infix:
    def __init__(self):
        self.list = []
        self.listPostfix = ""
        self.listO = []
    def infixToPostfix(self):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2,"^": 3,"(":0}
        for i in self.list:
            if i.isalpha():
                self.listPostfix += i
            elif i in "+-*/":
                while self.listO and precedence[i] <= precedence[self.listO[-1][0]]:
                    self.listPostfix += self.listO.pop()[0]
                self.listO.append((i , precedence[i]))
            elif i == "(":
                self.listO.append((i,0))
            elif i == ")":
                while self.listO and self.listO[-1][0] != "(":
                    self.listPostfix += self.listO.pop()[0]
                self.listO.pop()
        while self.listO:
            self.listPostfix += self.listO.pop()[0]
infix_to_postfix = Infix()
def main():
    """main"""
    infix_to_postfix.list = list(input())
    infix_to_postfix.infixToPostfix()
    print(infix_to_postfix.listPostfix)
main()