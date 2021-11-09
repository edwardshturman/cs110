grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def add_rows(table):
    col0_sum = 0
    col1_sum = 0
    col2_sum = 0

    for row in table:
        row_sum = 0
        for col in row:
            row_sum += col
            if row.index(col) == 0:
                col0_sum += col
            elif row.index(col) == 1:
                col1_sum += col
            elif row.index(col) == 2:
                col2_sum += col
        print('Row ' + str(table.index(row)) + ' total is: ' + str(row_sum))
    print('Column 0 total is: ' + str(col0_sum))
    print('Column 1 total is: ' + str(col1_sum))
    print('Column 2 total is: ' + str(col2_sum))


def main():
    add_rows(grid)


main()
