import time

def check_sort(list):

    for i in range(len(list)-1):

        if (list[i] > list[i+1]):
            return False

    return True
