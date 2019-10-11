def bubble_sort(list, selectOrder):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        if (str(selectOrder) == "lth"):
            for i in range(len(list) - 1):
                if sorted_list[i] > sorted_list[i + 1]: # swap
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1
                    print(swaps)
        elif (str(selectOrder) == "htl"):
            for i in range(len(list) - 1):
                if sorted_list[i] < sorted_list[i + 1]: # swap
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    swaps += 1
                    print(swaps)
        else:
            print("The second argument is incorrect!")
            print("Please select correct order. Either 'lth' for low to high sorting or 'htl' for high to low sorting.")
        if swaps == 0:
            is_sorted = True
    return sorted_list

print(bubble_sort([2, 3, 1], "lth"))
print(bubble_sort([2, 3, 1], "htl"))
print(bubble_sort([2, 5, 0, -2, 3, 1, 6, 6, 7], "htl"))
print(bubble_sort([2, 3, 1], "xyz"))