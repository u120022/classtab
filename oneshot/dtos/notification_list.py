from webclass_parser.models import Notification, NotificationList

# 表示用のデータの形式
NotificationListDto = list[Notification | None]


# 表示用のデータの形式へ変更
def from_notification_list(notification_list: NotificationList) -> NotificationListDto:
    count = notification_list.count

    dto: NotificationListDto = [None for _ in range(count)]
    for i in range(count):
        dto[i] = notification_list.get(i)

    return dto
