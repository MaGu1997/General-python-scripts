import random
'''Jump search'''
import math
def JumpSearch (lys1, val1):
    length = len(lys1)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys1[left] <= val1:
        right = min(length - 1, left + jump)
        if lys1[left] <= val1 and lys1[right] >= val1:
            break
        left += jump;
    if left >= length or lys1[left] > val1:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys1[i] <= val1:
        if lys1[i] == val1:
            return i
        i += 1
    return -i
'''Linear search'''
def LinearSearch(array1, element):
    for i in range (len(array1)):
        if array1[i] == element:
            return i
    return -1
'''Binary search'''
def BinarySearch(array2, val):
    first = 0
    last = len(array2)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if array2[mid] == val:
            index = mid
        else:
            if val<array2[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

'''Fibonacci Search'''
def FibonacciSearch(lys2, val2):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys2)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys2)-1))
        if (lys2[i] < val2):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys2[i] > val2):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys2)-1) and lys2[index+1] == val2):
        return index+1;
    return -1
'''Exponential Search'''
def ExponentialSearch(lys3, val3):
    if lys3[0] == val3:
        return 0
    index = 1
    while index < len(lys3) and lys3[index] <= val3:
        index = index * 2
    return BinarySearch( lys3[:min(index, len(lys3))], val3)
'''Interpolation Search'''
def InterpolationSearch(lys4, val4):
    low = 0
    high = (len(lys4) - 1)
    while low <= high and val4 >= lys4[low] and val4 <= lys4[high]:
        index = low + int(((float(high - low) / ( lys4[high] - lys4[low])) * ( val4 - lys4[low])))
        if lys4[index] == val4:
            return index
        if lys4[index] < val4:
            low = index + 1;
        else:
            high = index - 1;
    return -1

if __name__ == '__main__':
    # number of elements
    n = int(input("Length of list: "))
    randomlist = random.sample(range(1,99),n)
    print(randomlist)
    number=int(input("Search for number:"))
    print("Linear", LinearSearch(randomlist, number))
    print("Binary", BinarySearch(randomlist, number))
    print("Jump", JumpSearch(randomlist, number))
    print("Exponential", ExponentialSearch(randomlist, number))
    print("Fibonacci", FibonacciSearch(randomlist, number))
    print("Interpolation", InterpolationSearch(randomlist, number))
