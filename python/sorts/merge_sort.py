import random
import math

def merge_sort(list):
    if (len(list) == 1 or len(list) == 0):
        return list

    half = math.ceil(len(list)/2)

    left_half = list[0:half]
    right_half= list[half: len(list)]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    sorted_list = []

    while (True):

        if(left_half[0] < right_half[0]):
            sorted_list.append(left_half.pop(0))

        elif(left_half[0] > right_half[0]):
            sorted_list.append(right_half.pop(0))

        else:
            sorted_list.append(left_half.pop(0))
            sorted_list.append(right_half.pop(0))

        if (len(left_half) == 0):
            sorted_list = sorted_list + right_half
            return sorted_list

        if (len(right_half) == 0):
            sorted_list = sorted_list + left_half
            return sorted_list
    

def main():

    l = []
    for n in range(30):
        l.append(random.randint(-123, 100))

    print(l)

    print(merge_sort(l))

    print(l)

if __name__ == '__main__':
    main()
