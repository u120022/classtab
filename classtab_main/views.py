from django.http import HttpRequest, HttpResponse
from django.template import loader


def index(req: HttpRequest):
    template = loader.get_template("classtab_main/index.html")
    return HttpResponse(template.render(request=req))
