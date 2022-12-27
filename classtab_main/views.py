from django.http import HttpResponse


def index(req):
    return HttpResponse(b"Hello,world! I love python!")
