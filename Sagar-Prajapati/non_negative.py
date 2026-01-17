

def find_missing_number(lst):
    list_dict = {}
    for i in lst:
        list_dict[i]=True
    
    for i in range(len(lst)+1):
        if not list_dict.get(i):
            return i
        
    return None

lst = [0,1,2,3,4,5,7,8,9]
print(find_missing_number(lst))