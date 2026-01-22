#input array=[1,2,2,3] k=2
#ouput=[1,2]

#find out k most frequent elements

def k_most_element(input_array, k):
    base_dict = {}
    final_set = set()
    
    for i in input_array:
        if i in base_dict:
            base_dict[i] += 1
        else:
            base_dict[i] = 1
        
        if base_dict[i] >= k:
            final_set.add(i)
    
    return list(final_set)

print(k_most_element([1, 1 ,2, 2, 2, 3], 2))


