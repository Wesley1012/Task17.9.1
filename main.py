input_list = input("Введите последовательность чисел(int) через пробел:\n")

try:
    num_list = list(map(int, input_list.split()))
except ValueError:
    print("Ошибка: последовательность должна содержать целочисленные значения(int).")


try:
    element = int(input("Введите число для поиска:\n"))
except ValueError:
    print("Ошибка: введено не целочисленное значение(int).")

def sort_list(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def binary_search(array, element):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        if array[middle] == element:
            return middle
        elif array[middle] < element:
            low = middle + 1
        else:
            high = middle - 1
    return -1




sorted_list = sort_list(num_list)
print(f"Отсортированный список: {sorted_list}")

pos = binary_search(sorted_list, element)

if pos != -1:
        print(f"Число {element} найдено на позиции {pos}.")
else:
    print(f"Число {element} не найдено в последовательности.")

