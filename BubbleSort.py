def bubble_sort(list,order):
    sorted_list = list[:]
    is_sorted = False
    turns = 0
    while is_sorted == False:
        swaps = 0
        if order == "lth":
            for i in range(len(list) - 1): #loop through the list comparing number with next number
                if sorted_list[i] > sorted_list[i + 1]: # swap if the number is bigger than the previous number
                    temp = sorted_list[i] #temporary variable to store the to be swap number
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1 #print out a number of swap in ONE ITERATE
                    turns += swaps
        elif order == "htl":
            for i in range(len(list) - 1): 
                if sorted_list[i] < sorted_list[i + 1]:
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1
                    turns += swaps
        if swaps == 0:
            is_sorted = True
    print(turns)
    return sorted_list

print(bubble_sort([2, 1, 4, 5, 3],"htl"))


print(bubble_sort([2, 3, 1], "lth"))  # result: [1, 2, 3] 
print(bubble_sort([2, 3, 1], "htl"))  # result: [3, 2, 1]
print(bubble_sort([2, 5, 0, -2, 3, 1, 6, 6, 7], "htl")) # result: [7, 6, 6, 5, 3, 2, 1, 0, -2] 
print(bubble_sort([2, 3, 1], "xyz"))  # result: (message will be displayed)
print(bubble_sort([], "lth"))  # result: [] 
