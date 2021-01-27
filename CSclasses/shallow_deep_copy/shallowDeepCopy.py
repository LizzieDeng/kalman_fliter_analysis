# -*- coding: utf-8 -*-
"""
@Time: 2021/1/27 12:46
@Author: LizzieDeng
@File: shallowDeepCopy.py
@Description:
"""
# shallow copy: 用在切片时，浅拷贝就是指针拷贝
# deep copy: 深拷贝就是内容拷贝
import copy
a = [[1, 2], [2, 3]]
b = a[:]
# b[0][0] = 5
c = copy.deepcopy(a)
c[0][0] = 5
print(a)
print(c)


def all_nums(table):
    """Returns True if table contains only numbers
    Precondition: table is a (non-ragged) 2d List"""
    cnt = 0
    number_cnt = 0
    for row in table:
        for item in row:
            cnt += 1
            if type(item) in [int, float]:
                number_cnt += 1
    if cnt != number_cnt:
        print("table contains not only numbers")
        return False
    else:
        print("table contains only numbers")
        return True


def transpose(table):
    """Returns: copy of table with rows and columns swapped
    Precondition: table is a (non-ragged) 2d List"""
    new_table = []
    n_row = len(table)
    n_col = len(table[0])
    for col in range(n_col):
        each_col = []
        for row in range(n_row):
            each_col.append(table[row][col])
        new_table.append(each_col)
    # print(table)
    # print(new_table)
    return new_table


def add_one(table):
    """Adds one to every number in the table
    Preconditions: table is a 2d List,
    all table elements are int"""
    n_row = len(table)
    n_col = len(table[0])
    for row in range(n_row):
        for col in range(n_col):
            table[row][col] = table[row][col] + 1

    print(table)
    return table


def strip(table, col):
    """Removes column col from the given table
    Preconditions: table is a (non-ragged) 2d List,
    col valid column"""
    n_row = len(table)
    n_col = len(table[0])
    assert col < n_col, repr(col) + "要删除的列大于总列数！"
    for row in range(n_row):
        table[row] = table[row][:col]+table[row][col+1:]
    # print(table)
    return table


aa = [[1, 2, 3], [4, 5, 6]]
ret = all_nums(aa)
print(ret)
new_aa = transpose(aa)
print(new_aa)
add_table = add_one(aa)
print(add_table)
tb = [[1, 2, 3], [4, 5, 6]]
remove_tb = strip(tb, 2)
