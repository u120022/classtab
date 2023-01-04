from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from webclass_parser import Clazz, ClazzTable, auth, parse_clazz_table


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
    session_token = auth(username, password)
    if session_token is None:
        return HttpResponseBadRequest("認証に失敗しました。")

    # データの取得を試行
    clazz_table = parse_clazz_table(session_token)
    if clazz_table is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    # 表示用にデータの形式を変更
    clazz_table_view_model = from_clazz_table(clazz_table)

    context = {"clazz_table": clazz_table_view_model}

    return render(request, "oneshot/show_clazz_table.html", context)


# 表示用のデータの形式
ClassTableViewModel = list[list[Clazz | None]]

# 表示用のデータの形式へ変更
def from_clazz_table(clazz_table: ClazzTable) -> ClassTableViewModel:
    rows = clazz_table.row_count
    cols = clazz_table.col_count

    vm: ClassTableViewModel = [[None for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            vm[row][col] = clazz_table.get(col, row)

    return vm
