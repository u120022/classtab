from django.urls import path

from .views import clazz_table, index, info_list

app_name = "oneshot"
urlpatterns = [
    path("", index.index, name="index"),
    path("form_clazz_table", clazz_table.form, name="form_clazz_table"),
    path("show_clazz_table", clazz_table.show, name="show_clazz_table"),
    path("form_info_list", info_list.form, name="form_info_list"),
    path("show_info_list", info_list.show, name="show_info_list"),
]
