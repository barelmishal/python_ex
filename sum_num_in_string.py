s = '25 87 11 122 abc 45'
def sum_int_in_string(string):
    lst_nums = []
    split_string = string.split(' ')
    for is_num in split_string:
        if is_num.isnumeric():
            split_num = [int(num) for num in list(is_num)]
            nums_sum = sum(split_num)
            lst_nums.append(nums_sum)
    return lst_nums
print(sum_int_in_string(s))