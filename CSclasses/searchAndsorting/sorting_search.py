# -*- coding: utf-8 -*-
"""
@Time: 2021/1/29 16:25
@Author: LizzieDeng
@File: sorting_search.py
@Description:
"""


# 线性查找 效率 n
def linear_search(v, b):
    """Returns: first occurrence of v in b (-1 if not found)
    Precond: b a list of number, v a number
    """
    # ############# method 1
    # i = 0
    # while i < len(b) and b[i] != v:
    #     i += 1
    # if i == len(b):
    #     return -1
    # return i
    # ############## method 2
    # for i in range(len(b)):
    #     if b[i] == v:
    #         return i
    # return -1
    # ############## method 3
    i = len(b) - 1
    while i >= 0 and b[i] != v:
        i = i-1
    return i


def binary_search(v, b):
    """Returns: first occurrence of v in b (-1 if not found)
       Precond: b a list of number, v a number, 二分法查找
       """
    l = len(b)
    i = 0
    mid = (l + i) // 2
    while i < l:
        if v > b[mid]:
            i = mid+1
        else:
            l = mid
        mid = (l + i) // 2

    if i < len(b) and v == b[i]:
        return i
    return -1


def buble_sort(b):
    """
       1.  冒泡排序，遍历列表， 与相邻两个比较大小，小的排在前面
       Insertion Sort: Sorts the array b in n^2 time

       Parameter b: The sequence to sort
       Precondition: b is a mutable sequence (e.g. a list).
    """
    # ############ 方法一
    # for i in range(1, len(b)):
    #     for j in range(0, len(b)-i):
    #         if b[j] > b[j+1]:
    #             tmp = b[j]
    #             b[j] = b[j+1]
    #             b[j+1] = tmp
    # #             b[j], b[j + 1] = b[j + 1], b[j]
    # return b
    # ############ 方法二
    i = 0
    n = len(b)
    while i < n:
        j = i
        while j > 0:
            if b[j-1] > b[j]:
                tmp = b[j-1]
                b[j-1] = b[j]
                b[j] = tmp
            j -= 1
        i += 1
    return b


def select_sort(b):
    """
         2.  选择排序，遍历列表， 首先在未排列序列中找到最小序列，存放到序列的起始位置
         再从其余未排列序列中继续找最小的元素，放到已排序序列末尾
          Select Sort: Sorts the array b in n^2 time

          Parameter b: The sequence to sort
          Precondition: b is a mutable sequence (e.g. a list).
       """
    min_index = 0
    for i in range(len(b)):
        min_value = b[i]
        for j in range(i, len(b)):
            if b[j] < min_value:
                min_value = b[j]
                min_index = j
        tmp = b[i]
        b[i] = b[min_index]
        b[min_index] = tmp

    return b


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


unsorted_list = [5, 0, 1, 9, 10, 2]
sorted_list = buble_sort(unsorted_list)
print('sorted_list:', sorted_list)
select_list = select_sort(unsorted_list)
print("sorted_list is {}".format(buble_sort(unsorted_list)))
print("select_list is {}".format(select_list))
print("bubbleSort is {}".format(bubbleSort(unsorted_list)))


bin_list = [0, 4, 7, 9, 11, 13, 20, 22, 26]
ret_bin = binary_search(122, bin_list)
print(ret_bin)
ret = linear_search(0, [1, 2, 3])
print('ret is {}'.format(ret))


