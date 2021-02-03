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
        i = i - 1
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
            i = mid + 1
        else:
            l = mid
        mid = (l + i) // 2

    if i < len(b) and v == b[i]:
        return i
    return -1


# 1.  冒泡排序
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
            if b[j - 1] > b[j]:
                tmp = b[j - 1]
                b[j - 1] = b[j]
                b[j] = tmp
            j -= 1
        i += 1
    return b


# 2.  选择排序
def select_sort(b):
    """
         2.  选择排序，遍历列表， 首先在未排列序列中找到最小序列，存放到序列的起始位置
         再从其余未排列序列中继续找最小的元素，放到已排序序列末尾
          Select Sort: Sorts the array b in n^2 time

          Parameter b: The sequence to sort
          Precondition: b is a mutable sequence (e.g. a list).
       """

    for i in range(len(b)-1):
        min_index = i
        for j in range(i+1, len(b)):
            if b[j] < b[min_index]:
                min_index = j
        if i != min_index:
            tmp = b[i]
            b[i] = b[min_index]
            b[min_index] = tmp

    return b


# 3.  插入排序
def insert_sort(b):
    """
     3.  插入排序，将第一个元素当成有序序列，遍历第二个元素到最后一个元素，将每个元素插入有序序列的适当位置， 若插入的元素与有序序列中某个元素相等，则插入到该元素的后面
      Select Sort: Sorts the array b in n^2 time

      Parameter b: The sequence to sort
      Precondition: b is a mutable sequence (e.g. a list).

    """
    for i in range(1, len(b)):
        # ############ 方法一
        # # 将该元素与有序序列进行比较插入，默认第一个元素为有序序列
        # for j in range(i):
        #     if i == 1:
        #         if b[j] >= b[i]:
        #             tmp = b[j]
        #             b[j] = b[i]
        #             b[i] = tmp
        #     if b[j] <= b[i] <= b[j + 1]:
        #         tmp = b[j + 1]
        #         b[j + 1] = b[i]
        #         b[i] = tmp
        # ############ 方法二
        j = i
        tmp = b[i]  # 记录要插入的数据
        while j > 0 and b[j-1] > tmp:  # 从右边开始比较插入
            b[j] = b[j-1]
            b[j-1] = tmp
            j -= 1

    return b


# 4. 希尔排序
def shell_sort(b):
    """
       4. 希尔排序，把较大的数据集合选定一个增量进行分割成若干个小组，然后对每个小组进行插入排序，然后缩小增量为以前的一半再进行插入排序，如此循环，直到增量最后为1时对全部元素进行插入排序结束，
       参考博客： https://blog.csdn.net/qq_39207948/article/details/80006224
        Select Sort: Sorts the array b in n^2 time

        Parameter b: The sequence to sort
        Precondition: b is a mutable sequence (e.g. a list).

      """
    l = len(b)
    gap = l // 2
    while gap > 0:
        for i in range(gap):
            # 提取每组数据进行插入排序
            id_list = [id for id in range(i, l, gap)]
            array_list = [b[id] for id in range(i, l, gap)]
            sorted_list = insert_sort(array_list)
            for x, y in zip(id_list, sorted_list):
                b[x] = y
        gap = gap // 2
    return b


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ####################### 查找 #############
bin_list = [0, 4, 7, 9, 11, 13, 20, 22, 26]
ret_bin = binary_search(122, bin_list)
print("ret_bin is {}".format(ret_bin))
ret = linear_search(0, [1, 2, 3])
print('ret is {}'.format(ret))

#  ####################### 排序 #############

unsorted_list = [5, 0, 1, 9, 10, 2, -4, 7]
# 1. 冒泡排序
sorted_list = buble_sort(unsorted_list.copy())
print('sorted_list is {}'.format(sorted_list))
# 2. 选择排序
select_list = select_sort(unsorted_list.copy())
print("select_list is {}".format(select_list))
# 3. 插入排序
insert_list = insert_sort(unsorted_list.copy())
print("insert_list is {}".format(insert_list))
# 4. 希尔排序
shell_list = shell_sort(unsorted_list.copy())
print("shell_list is  {} ".format(shell_list))





