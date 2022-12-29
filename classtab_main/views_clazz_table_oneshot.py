from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import loader
from webclass_parser import Clazz, auth, parse_clazz_table


def form(req: HttpRequest):
    template = loader.get_template("classtab_main/form_clazz_table_oneshot.html")
    return HttpResponse(template.render(request=req))


def show(req: HttpRequest):
    if "username" not in req.POST or "password" not in req.POST:
        return HttpResponseBadRequest("ユーザ名とパスワードが入力されていません。")

    username = req.POST["username"]
    password = req.POST["password"]

    session_token = auth(username, password)
    if session_token is None:
        return HttpResponseBadRequest("認証に失敗しました。")

    clazz_table = parse_clazz_table(session_token)
    if clazz_table is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    clazz_table_vm: list[list[Clazz | None]] = [
        [None for _ in range(clazz_table.col_count)]
        for _ in range(clazz_table.row_count)
    ]
    for col in range(clazz_table.col_count):
        for row in range(clazz_table.row_count):
            clazz_table_vm[row][col] = clazz_table.get(col, row)

    context = {"clazz_table": clazz_table_vm}

    template = loader.get_template("classtab_main/show_clazz_table_oneshot.html")
    return HttpResponse(template.render(context, req))
