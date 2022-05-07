'''Написати власну помилку'''

class SecondElementError(Exception):
    '''This element cannot be printed into int. It is a repetition'''
    pass

list_of_num = [1,2,7,4,7]
all_nums = []
for el in list_of_num:
    if el in all_nums:
        raise SecondElementError
    else:
        all_nums.append(el)