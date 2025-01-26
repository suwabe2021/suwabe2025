from django.shortcuts import render
from django.views import View
import json

#公開したくないものをjsonに入れてあるのでそれを読み込む
try:
    with open("ignore.json") as redirect_file:
        redirect_data = json.load(redirect_file)
except FileNotFoundError:
    raise RuntimeError("ファイルが見つからない: redirect_file.json")
except json.JSONDecodeError:
    raise RuntimeError("JSON形式の解析中にエラーが発生: redirect_file.json")

truepass = redirect_data["REDIRECT_KEY"]

# 共通処理関数
def render_with_context(request, passwd):
    context = {
        "passwd": passwd,
        "truepass": truepass,
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