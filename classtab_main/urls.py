from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "form_clazz_table_oneshot",
        views.form_clazz_table_oneshot,
        name="form_clazz_table_oneshot",
    ),
    path(
        "show_clazz_table_oneshot",
        views.show_clazz_table_oneshot,
        name="show_clazz_table_oneshot",
    ),
]
