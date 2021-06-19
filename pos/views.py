from django.shortcuts import render, get_object_or_404
from pos.models import Menu, Order

# Create your views here.

def home(request):
    return render(request, 'pos/home.html')

def daftar_menu(request, order_id):
    menu_list = Menu.objects.all()
    order = get_object_or_404(Order, pk=order_id)

    return render(request,
                  'pos/daftar_menu.html',
                  {'menus': menus,
                   'order': order})


