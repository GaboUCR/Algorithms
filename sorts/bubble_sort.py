from helper import check_sort
import random
import copy

#mutates list
def bubble_sort_2(list):
    swap = False

    while (not swap):
        swap = True

        for e in range(1,len(list)):
            if (list[e] < list[e-1]):
                swap = False
                temp = list[e]
                list[e] = list[e-1]
                list[e-1] = temp


def bubble_sort(list):
    sorted_list = copy.deepcopy(list)
    new_list = []

    while (True):
        cur_max = sorted_list[0]
        new_list = []

        for e in range(1,len(sorted_list),1):

            if (cur_max >= sorted_list[e]):
                new_list.append(sorted_list[e])

            elif (cur_max < sorted_list[e]):
                new_list.append(cur_max)
                cur_max = sorted_list[e]

        new_list.append(cur_max)

        if (check_sort(new_list)):
            return new_list

        sorted_list = copy.deepcopy(new_list)

def main():
    l = []
    for n in range(10):
        l.append(random.randint(-1211, 1000))

    print(l)
    bubble_sort_2(l)
    print(l)

if __name__ == '__main__':
    main()
