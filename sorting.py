import time

'''bubble sort'''
def bubble_sort(array):

    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array
'''insertion sort'''
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array

'''quick sort'''
from random import randint
def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)
    
'''tim sort'''
def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def timsort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2
    return array
'''selection sort'''
def selection_sort(L):
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

        return L


if __name__ == '__main__':
    start =time.time()
    choice=int(input("Random list of numbers?\n1.Yes,\n2.No\n"))
    if choice==2:
        # number of elements
        n = int(input("Enter number of elements : "))

        # Below line read inputs from user using map() function
        a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
    else:
        import random
        n = int(input("Length of list:"))
        a = random.sample(range(1,99),n)
        print(a)
        print("\n")
    # print("\nList is - \n   ", a)
    print("Insertion sort", insertion_sort(a))
    print("bubble_sort", bubble_sort(a))
    print("timsort", timsort(a))
    print("quicksort", quicksort(a))
    print("selection_sort", selection_sort(a))
    end = time.time()
    print(f"Time taken to run program:,{end-start}")
