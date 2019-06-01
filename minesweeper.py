def is_bomb(a, b):
    return mine_field[a][b] == -1


def update_sides(row, col):
    row_start = max(row - 1, 0)
    col_start = max(col - 1, 0)
    row_end = min(row + 1, n_rows - 1)
    col_end = min(col + 1, n_columns - 1)
    for ri in range(row_start, row_end + 1):
        for ci in range(col_start, col_end + 1):
            if not is_bomb(ri, ci):
                mine_field[ri][ci] += 1


if __name__ == '__main__':
    bomb_list = eval(input("List of bombs: "))
    n_columns = int(input("No. of columns: "))
    n_rows = int(input("No. of rows: "))
    mine_field = [[0 for i in range(n_columns)] for j in range(n_rows)]
    for bomb in bomb_list:
        r = bomb[0]
        c = bomb[1]
        mine_field[r][c] = -1
        update_sides(r, c)
    print(mine_field)
