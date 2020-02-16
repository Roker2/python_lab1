import argparse
import sys


# Разбиение Ломута
def partition_L(data, left, right):
    pivot = data[right]
    i = left
    print(range(left, right - 1))
    for j in range(left, right - 1):
        if data[j] <= pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[right] = data[right], data[i]
    return i


def partition_H(data, left, right):
    pivot = data[(left + right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while data[i] < pivot:
            i += 1
        j -= 1
        while data[j] > pivot:
            j -= 1
        if i >= j:
            return j
        data[i], data[j] = data[j], data[i]


def quicksort(data, left, right):
    if left < right:
        p = partition_H(data, left, right)
        quicksort(data, left, p)
        quicksort(data, p + 1, right)


def merge(left_data, right_data):
    sorted_data = []
    left_index = 0
    right_index = 0
    for _ in range(len(left_data) + len(right_data)):
        if (left_index < len(left_data)) & (right_index < len(right_data)):
            if left_data[left_index] <= right_data[right_index]:
                sorted_data.append(left_data[left_index])
                left_index += 1
            else:
                sorted_data.append(right_data[right_index])
                right_index += 1
        elif left_index == len(left_data):
            for value in right_data[right_data:]:
                sorted_data.append(value)
            break
        elif right_index == len(right_data):
            for value in left_data[left_index:]:
                sorted_data.append(value)
            break
    return sorted_data


def merge_sort(data):
    if len(data) <= 1:
        return data
    center = len(data) // 2
    return merge(merge_sort(data[:center]),
                 merge_sort(data[center:]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='Type program: one, two')
    parser.add_argument('--file', type=str, help='Path to file')
    # print(parser.parse_args())

    if not vars(parser.parse_args())['type']:
        print('You didn\'t choose program type')
        sys.exit()

    if not vars(parser.parse_args())['file']:
        print('You didn\'t choose file')
        sys.exit()

    if vars(parser.parse_args())['type'] == 'help':
        parser.print_help()
        sys.exit()

    if (vars(parser.parse_args())['type'] == 'one') | (vars(parser.parse_args())['type'] == 'two'):
        file = open(vars(parser.parse_args())['file'], 'r')
        string = file.read()
        file.close()
        string = string.replace('!', '')
        string = string.replace('?', '')
        string = string.replace('.', '')
        string = string.replace(',', '')
        string = string.replace(':', '')
        string = string.replace(';', '')
        # string = string.lower()
        MyDictionary = {}
        for word in string.split():
            if word in MyDictionary.keys():
                MyDictionary[word] += 1
            else:
                MyDictionary[word] = 1
        print(MyDictionary)

    if vars(parser.parse_args())['type'] == 'two':
        maximum = 0
        for value in MyDictionary.values():
            if value > maximum:
                maximum = value
        #    print(maximum)
        string = ''
        while (len(string.split()) != 10) & (maximum != 0):
            for word in MyDictionary.keys():
                if MyDictionary[word] == maximum:
                    string += word + ' '
                if len(string.split()) == 10:
                    break
            maximum -= 1
        print(string)

    if vars(parser.parse_args())['type'] == 'three':
        file = open(vars(parser.parse_args())['file'], 'r')
        string = file.read()
        file.close()
        mas = []
        for value in string.split():
            mas.append(int(value))
        print(mas)
        quicksort(mas, 0, len(mas) - 1)
        print(mas)
    # print(mas[:(len(mas) // 2)])

    if vars(parser.parse_args())['type'] == 'four':
        file = open(vars(parser.parse_args())['file'], 'r')
        string = file.read()
        file.close()
        mas = []
        for value in string.split():
            mas.append(int(value))
        print(mas)
        print(merge_sort(mas))
