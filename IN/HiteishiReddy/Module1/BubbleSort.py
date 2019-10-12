def Ascending_bubble_sort(list):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(len(list) - 1):
            if sorted_list[i] > sorted_list[i + 1]: # swap
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                swaps += 1
                print(swaps)
        if swaps == 0:
            is_sorted = True
    return sorted_list

def Descending_bubble_sort(list):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(len(list) - 1):
            if sorted_list[i] < sorted_list[i - 1]: # swap
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i - 1]
                sorted_list[i - 1] = temp
                swaps += 1
                # print(swaps)
        if swaps == 0:
            is_sorted = True
    return sorted_list

lst = [2, 1, 3]
print('type A for Ascending  or D for  descending: ?')
c = (input())
if c == 'A':
    print(Ascending_bubble_sort(lst))

elif c == 'D':
    print(Descending_bubble_sort(lst))


# print(bubble_sort(lst))