
def get_profit_estimate(l):
    lowest_value = l[0]
    lowest_index = 0
    for i in range(1,len(l)):
        if l[i] < lowest_value:
            lowest_value = l[i]
            lowest_index = i
    l2 = l[lowest_index:]  # [2, 9, 4, 10, 9]
    max_value = l2[0]
    #max_index = 0
    for i in range(1,len(l2)):
        if l2[i] > max_value:
            max_value = l2[i]
            #max_index = i
    result = max_value - lowest_value
    if result == 0:
        return None
    return result


if __name__=='__main__':
    #prices = [7,1,8,5,2,9,4,20,9]
    prices = [7,6,4,3,1]
    r = get_profit_estimate(prices)
    print(r)






















