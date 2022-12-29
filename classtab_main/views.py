from django.http import HttpRequest, HttpResponse


def index(req: HttpRequest):
    return HttpResponse(b"Hello,world! I love python!")
