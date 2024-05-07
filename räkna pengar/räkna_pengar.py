money_list = [20, 10, 6, 3]
""" 

20 + 20 + 30 + 30 = 100

 """

def count_money():
    sum = 0
    sum += money_list[0] * 1
    sum += money_list[1] * 2
    sum += money_list[2] * 5
    sum += money_list[3] * 10
    
    return sum

print(count_money())