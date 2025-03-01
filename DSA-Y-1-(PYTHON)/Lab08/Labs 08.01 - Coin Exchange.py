"""Labs 08.01 - Coin Exchange"""
import json
def coin(x,l):
    """Labs 08.01 - Coin Exchange"""
    sum = x
    coin_int = 0
    sum_money = 0
    l_c = l.copy()
    for i in l_c:
        can_change = sum//int(i)
        if l_c[i] >= can_change:
            really_change = can_change
        else:
            really_change = l_c[i]
        coin_int += really_change
        sum_money += really_change*int(i)
        l_c[i] = really_change
        sum -= really_change*int(i)
    print("Amount:",x)
    if sum_money==x:
        print("Coin exchange result:")
        for i in l_c:
            print(f"  {i} baht = {l_c[i]} coins")
        print("Number of coins:",coin_int)
    else:
        print("Coins are not enough.")
coin(int(input()),json.loads(input()))
