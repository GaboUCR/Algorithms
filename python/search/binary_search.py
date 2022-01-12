import math
# list must be sorted
# e must be able to be compatible with comparisons

def binary_search (list, e):
    max, min = len(list), 0
    index = math.ceil((max+min)/2)
    found = False

    while (not found):

        if (list[index] == e):
            found = True
            break

        elif (list[index] < e):
            min = index

        elif (list[index] > e):
            max = index

        #max and min being at a distance of 1 means there's no more elements to look
        if (max+1 == min or min+1 == max):
            break

        index = math.ceil((max+min)/2)

    return found


def main():

    l = [4, 7,8, 10, 100, 230, 506, 1000]

    print(binary_search(l, 1))

if __name__ == '__main__':
    main()
