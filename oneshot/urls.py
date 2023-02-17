from django.urls import path

from .views import clazz_table, index, notification_list

app_name = "oneshot"
urlpatterns = [
    path("", index.index, name="index"),
    path("form_clazz_table", clazz_table.form, name="form_clazz_table"),
    path("show_clazz_table", clazz_table.show, name="show_clazz_table"),
    path(
        "form_notification_list", notification_list.form, name="form_notification_list"
    ),
    path(
        "show_notification_list", notification_list.show, name="show_notification_list"
    ),
]
