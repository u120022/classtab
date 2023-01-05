from webclass_parser import Clazz, ClazzTable

# 表示用のデータの形式
ClazzTableDto = list[list[Clazz | None]]


# 表示用のデータの形式へ変更
def from_clazz_table(clazz_table: ClazzTable) -> ClazzTableDto:
    rows = clazz_table.row_count
    cols = clazz_table.col_count

    dto: ClazzTableDto = [[None for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            dto[row][col] = clazz_table.get(col, row)

    return dto
