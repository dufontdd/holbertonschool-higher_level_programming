#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            div = 0
        finally:
            result.append(div)
    
    return result
