from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from webclass_parser.request import auth_user, fetch_clazz_table

from oneshot.dtos.clazz_table import from_clazz_table


# ユーザ情報の入力フォーム用ページ
def form(request: HttpRequest) -> HttpResponse:
    return render(request, "oneshot/form_clazz_table.html", {})


# 取得データの表示用ページ
def show(request: HttpRequest) -> HttpResponse:
    # リクエストの検証
    if "username" not in request.POST or "password" not in request.POST:
        return HttpResponseBadRequest("ユーザ名とパスワードが入力されていません。")

    username = request.POST["username"]
    password = request.POST["password"]

    # 認証を試行
    session_token = auth_user(username, password)
    if session_token is None:
        return HttpResponseBadRequest("認証に失敗しました。")

    # データの取得を試行
    clazz_table = fetch_clazz_table(session_token)
    if clazz_table is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    # 表示用にデータの形式を変更
    clazz_table_dto = from_clazz_table(clazz_table)

    context = {"clazz_table": clazz_table_dto}

    return render(request, "oneshot/show_clazz_table.html", context)
