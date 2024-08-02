import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def caijiewei(request):
    return HttpResponse(r"我喜欢 caijiewei!!!")

def user(request):
    return HttpResponse(r"User")

def clint4(request):
    name1 = "Clark"
    name2 = ["Olsen", "ClarkHu", "LLGreat"]
    name3 = {"hyq": 1, "zlp": 2}
    name4 = [{"hyq": 1, "zlp": 2},
             {"hyq": 3, "zlp": 6},
             {"hyq": 4, "zlp": 9}]
    return render(request, "test1.html", {"n1": name1, "n2": name2, "n3": name3, "n4": name4})

def liantong(request):

    xinwenlist = [

        {"title": "中共中国联合网络通信集团有限公司党组", "time": "2024-07-08"},
        {"title": "中国联通精彩亮相2024世界人工智能大会", "time": "2024-07-08"},
           ]

    print("---------------------------")

    return render(request, "liantong.html", {"xinwenlist": xinwenlist})

    # return HttpResponse("lalala")

    # return render(request,"liantong.html",)


def unitest(request):

    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    re = requests.get("https://www.chinaunicom.com.cn/43/menu01/1/column05", headers=head)
    cont = re.content
    print(re)
    print(cont)