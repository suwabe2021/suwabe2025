from django.shortcuts import render
from django.views import View
from django.conf import settings

SOCIAL_AUTH_LINE_KEY = settings.SOCIAL_AUTH_LINE_KEY
SOCIAL_AUTH_LINE_SECRET = settings.SOCIAL_AUTH_LINE_SECRET
LINE_REDIRECT_URL = settings.LINE_REDIRECT_URL
REDIRECT_KEY = settings.REDIRECT_KEY

# 共通処理関数
def render_with_context(request, passwd):
    context = {
        "passwd": passwd,
        "truepass": REDIRECT_KEY,
    }
    return render(request, "login/index.html", context)

class IndexView(View):
    def get(self, request, passwd=0):
        return render_with_context(request, passwd)

#特定URLから来た場合のみLINEログインに進める仕組み
class Authentication(View):
    def get(self, request, passwd):
        return render_with_context(request, passwd)

index = IndexView.as_view()
authentication = Authentication.as_view()