
def add_num(lst):
    if len(lst)<2:
        return False
    l1 = set(lst)
    for i in lst:
        if -i in l1:
            return True
    return False
lst = [1,2,3,4,-1,-2,-3,-4]
print(add_num(lst))