from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import loader
from webclass_parser import Info, auth, parse_info_list


def form(req: HttpRequest):
    template = loader.get_template("classtab_main/form_info_list_oneshot.html")
    return HttpResponse(template.render(request=req))


def show(req: HttpRequest):
    if "username" not in req.POST or "password" not in req.POST:
        return HttpResponseBadRequest("ユーザ名とパスワードが入力されていません。")

    username = req.POST["username"]
    password = req.POST["password"]

    session_token = auth(username, password)
    if session_token is None:
        return HttpResponseBadRequest("認証に失敗しました。")

    info_list = parse_info_list(session_token)
    if info_list is None:
        return HttpResponseBadRequest("データの取得に失敗しました。")

    info_list_vm: list[Info | None] = [None for _ in range(info_list.count)]
    for i in range(info_list.count):
        info_list_vm[i] = info_list.get(i)

    context = {"info_list": info_list_vm}

    template = loader.get_template("classtab_main/show_info_list_oneshot.html")
    return HttpResponse(template.render(context, req))
