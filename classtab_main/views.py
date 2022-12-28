from django.http import HttpRequest, HttpResponse
from django.template import loader
from webclass_parser import Clazz, auth, parse_clazz_table


def index(req: HttpRequest):
    return HttpResponse(b"Hello,world! I love python!")


def form_clazz_table_oneshot(req: HttpRequest):
    template = loader.get_template("classtab_main/form_clazz_table_oneshot.html")
    return HttpResponse(template.render(request=req))


def show_clazz_table_oneshot(req: HttpRequest):
    username = req.POST["username"]
    if username is None:
        return HttpResponse()

    password = req.POST["password"]
    if password is None:
        return HttpResponse()

    session_token = auth(username, password)
    if session_token is None:
        return HttpResponse()

    clazz_table = parse_clazz_table(session_token)
    if clazz_table is None:
        return HttpResponse()

    clazz_table_transposed: list[list[Clazz | None]] = [
        [None for _ in range(clazz_table.col_count)]
        for _ in range(clazz_table.row_count)
    ]
    for col in range(6):
        for row in range(8):
            clazz_table_transposed[row][col] = clazz_table.get(col, row)

    context = {"clazz_table_transposed": clazz_table_transposed}

    template = loader.get_template("classtab_main/show_clazz_table_oneshot.html")
    return HttpResponse(template.render(context, req))
