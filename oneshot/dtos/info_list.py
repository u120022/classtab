from webclass_parser import Info, InfoList

# 表示用のデータの形式
InfoListDto = list[Info | None]


# 表示用のデータの形式へ変更
def from_info_list(info_list: InfoList) -> InfoListDto:
    count = info_list.count

    dto: InfoListDto = [None for _ in range(count)]
    for i in range(count):
        dto[i] = info_list.get(i)

    return dto
