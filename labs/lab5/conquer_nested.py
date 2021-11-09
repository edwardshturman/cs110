grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def add_rows(table):
    for row in table:
        row_sum = 0
        for col in row:
            row_sum += col
        print('Row ' + str(table.index(row)) + ' total is: ' + str(row_sum))


def main():
    add_rows(grid)


main()
