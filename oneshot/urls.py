from django.urls import path

from . import views, views_clazz_table, views_info_list

app_name = "oneshot"
urlpatterns = [
    path("", views.index, name="index"),
    path("form_clazz_table", views_clazz_table.form, name="form_clazz_table"),
    path("show_clazz_table", views_clazz_table.show, name="show_clazz_table"),
    path("form_info_list", views_info_list.form, name="form_info_list"),
    path("show_info_list", views_info_list.show, name="show_info_list"),
]
