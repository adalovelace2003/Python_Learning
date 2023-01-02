def greater_than_num_5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 2, 3, 4, 5, 6, 6, 4, 453, 7, 6, 65, 4, 1]

print(list(filter(greater_than_num_5,l )))
