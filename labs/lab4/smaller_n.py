def smaller_than_n_list(input_list, n):
    output_list = []
    for num in input_list:
        if num < n:
            output_list.append(num)
    return output_list


def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 5
    print('Number: ' + str(n))
    print('List of numbers: ' + str(input_list))
    print('List of numbers smaller than ' + str(n) + ': ' + str(smaller_than_n_list(input_list, n)))


main()
