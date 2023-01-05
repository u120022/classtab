from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from webclass_parser import auth, parse_info_list

from oneshot.dtos.info_list import from_info_list


# ユーザ情報の入力フォーム用ページ
def form(request: HttpRequest) -> HttpResponse:
    return render(request, "oneshot/form_info_list.html", {})


# 取得データの表示用ページ
def show(request: HttpRequest) -> HttpResponse:
    # リクエストの検証
    if "username" not in request.POST or "password" not in request.POST:
        return HttpResponseBadRequest("ユーザ名とパスワードが入力されていません。")

    username = request.POST["username"]
    password = request.POST["password"]

    # 認証を試行
    session_token = auth(username, password)
    if session_token is None:
        return HttpResponseBadRequest("認証に失敗しました。")

    # データの取得を試行
    info_list = parse_info_list(session_token)
    if info_list is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    # 表示用にデータの形式を変更
    info_list_dto = from_info_list(info_list)

    context = {"info_list": info_list_dto}

    return render(request, "oneshot/show_info_list.html", context)
