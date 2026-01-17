#Brute Force Approach

def add_num_brut(lst):
    n=len(lst)
    for i in range(0,n):
        for j in range(i+1,n):
            if lst[i]+lst[j]==0:
                return True
    return False




# Hash Set Approach
def add_num(lst):
    if len(lst)<2:
        return False
    l1 = set(lst)
    for i in lst:
        if -i in l1:
            return True
    return False
#lst = [1,2,3,4,-1,-2,-3,-4]
#print(add_num_brut(lst))

# Two Pointer Approach

def add_num_two_pointer(lst):
    lst.sort()
    left,right=0,len(lst)-1
    while left < right:
        s= lst[left]+ lst[right]
        if s==0:
            return True
        elif s<0:
            left+=1
        else:
            right+=-1
    return False

lst = [1,2,3,4,-1,-2,-3,-4]
print(add_num_two_pointer(lst))