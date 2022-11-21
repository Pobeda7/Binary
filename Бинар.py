RawInput = input('Введите последовательность чисел через пробел: ')
int_array = [int(i) for i in RawInput.split (' ') if i.isdigit()]
list.sort(int_array)
print(int_array)

num = int(input('Введите число: '))
print(num)

def binary_search(int_array, num, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if int_array[middle] == num:
        return middle -1
    elif num < int_array[middle]:
        return binary_search(int_array, num, left, middle - 1)
    else:
        return binary_search(int_array, num, right, middle + 1)
        
print(f'Индекс числа:', (binary_search(int_array, num, 0, len(int_array)-1)))
