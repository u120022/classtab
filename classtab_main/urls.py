from django.urls import path

from . import views, views_clazz_table_oneshot, views_info_list_oneshot

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "form_clazz_table_oneshot",
        views_clazz_table_oneshot.form,
        name="form_clazz_table_oneshot",
    ),
    path(
        "show_clazz_table_oneshot",
        views_clazz_table_oneshot.show,
        name="show_clazz_table_oneshot",
    ),
    path(
        "form_info_list_oneshot",
        views_info_list_oneshot.form,
        name="form_info_list_oneshot",
    ),
    path(
        "show_info_list_oneshot",
        views_info_list_oneshot.show,
        name="show_info_list_oneshot",
    ),
]
