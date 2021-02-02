# -*- coding: utf-8 -*-
"""
@Time: 2021/2/2 13:19
@Author: LizzieDeng
@File: crcDesign.py
@Description:
"""


def CRC_3(input_string):
    """
    CRC 正向算法
    CRC-3标准的h(x) = x^3 + x^1 + 1   --> 1011
    :return:
    """
    # 根据CRC-3标准将输入的字符串后面添加三个0
    # 将二进制转化成
    input_string += '000'
    input_string_len = len(input_string)
    input_bin = bytes(input_string, encoding='utf-8')
    crc3_string = '1011' + (input_string_len - 4) * '0'
    crc_3_bin = bytes(crc3_string, encoding='utf-8')
    loop_flag = True
    while loop_flag:
        # 将二进制转化成十进制
        input_dec = int(input_bin, 2)
        crc_3_dec = int(crc_3_bin, 2)
        # 异或操作
        result_dec = input_dec ^ crc_3_dec
        result_bin = bin(result_dec)
        # 对二进制结果长度进行判断，若小于等于4终止循环
        if len(str(result_bin[2:])) <= 4:
            loop_flag = False
        else:
            input_bin = result_bin
            crc_3_bin = '1011' + (len(result_bin)-2-4) * '0'

    print("result_bin", result_bin)
    print("result_dec", result_dec)


def CRC_algorithm(crc_type, input_string):
    """
    crc_type : 3, 5, 8
    CRC 正向算法
    CRC-3标准的h(x) = x^3 + x^1 + 1   --> 1011
    :return:
    """
    # 根据CRC-3标准将输入的字符串后面添加三个0
    # 将二进制转化成
    if crc_type == 3:
        crc_standred = '1011'
    elif crc_type == 8:
        crc_standred = '111010101'

    input_string += '0'*crc_type
    input_string_len = len(input_string)
    input_bin = bytes(input_string, encoding='utf-8')
    crc3_string = crc_standred + (input_string_len - len(crc_standred)) * '0'
    crc_3_bin = bytes(crc3_string, encoding='utf-8')
    loop_flag = True
    while loop_flag:
        # 将二进制转化成十进制
        input_dec = int(input_bin, 2)
        crc_3_dec = int(crc_3_bin, 2)
        # 异或操作
        result_dec = input_dec ^ crc_3_dec
        result_bin = bin(result_dec)
        # 对二进制结果长度进行判断，若小于等于crc_standred长度终止循环
        if len(str(result_bin[2:])) <= len(crc_standred):
            loop_flag = False
        else:
            input_bin = result_bin
            crc_3_bin = crc_standred + (len(result_bin) - 2 - len(crc_standred)) * '0'

    print("result_bin", result_bin)
    print("result_dec", result_dec)


crc_type, input_string = 3, '1100010100000000000000001000'
CRC_algorithm(crc_type, input_string)


def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]


def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ('1' not in ''.join(input_padded_array)[len_input:])


a = bin(0x0C500008)
b = bin(int('0C500008', 16))
# a = '1001100010100000000000000001'
print('a', a)
print('b', b)
value = crc_remainder(a, '1011', '0')
check = crc_check(a, '1011', value)
print(value, check)
