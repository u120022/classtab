from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from webclass_parser.request import auth_user, fetch_notification_list

from oneshot.dtos.notification_list import from_notification_list


# ユーザ情報の入力フォーム用ページ
def form(request: HttpRequest) -> HttpResponse:
    return render(request, "oneshot/form_notification_list.html", {})


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
    notification_list = fetch_notification_list(session_token)
    if notification_list is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    # 表示用にデータの形式を変更
    notification_list_dto = from_notification_list(notification_list)

    context = {"notification_list": notification_list_dto}

    return render(request, "oneshot/show_notification_list.html", context)
