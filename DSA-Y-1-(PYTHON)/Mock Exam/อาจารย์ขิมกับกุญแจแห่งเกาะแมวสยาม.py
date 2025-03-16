"""อาจารย์ขิมกับกุญแจแห่งเกาะแมวสยาม"""
def main(string):
    """อาจารย์ขิมกับกุญแจแห่งเกาะแมวสยาม"""
    stack = []
    for index,j in enumerate(string):
        if not stack:
            stack.append(j)
        else:
            if j not in stack:
                if ord(stack[-1]) > ord(j) :
                    if stack[-1] in string[index:]:
                        stack = []
                stack.append(j)
    stack_str = ""
    for i in stack:
        stack_str+=i
    print(stack_str)
main(input())
