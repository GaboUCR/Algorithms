import random

def selection_sort_2(list):
    prefix_index = 0

    while (prefix_index != len(list)):
        for i in range(prefix_index,len(list)):

            if (list[i] < list[prefix_index]):
                list[i], list[prefix_index] = list[prefix_index], list[i]

        prefix_index += 1



#this sort implementation mutates list argument, not a recommended practice
def selection_sort(list):
    done = False
    sorted_list= []

    while (not done):
        min = 0

        for i in range(1, len(list)):
            if (list[i] < list[min]):
                min = i

        sorted_list.append(list.pop(min))

        if (len(list) == 0):
            return sorted_list


def main():
    l = []
    for n in range(10):
        l.append(random.randint(-1211, 1000))
    #
    # print(l)
    # print(selection_sort(l))
    print(l)
    selection_sort_2(l)
    print(l)

if __name__ == '__main__':
    main()
