from django.shortcuts import render

# Create your views here.
from App.models import Wheel, Nav, Mustbuy


def home(request):
    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = Mustbuy.objects.all()

    data = {
        'title' : '首页',
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
    }

    return render(request, 'home/home.html',context=data)


def market(request):
    return render(request, 'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')