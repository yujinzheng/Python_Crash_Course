from django.shortcuts import render
from .models import Pizza

def index(request):
    """pizzas的主页"""
    return render(request, 'pizzas/index.html')

def names(request):
    """所有披萨的页面"""
    names = Pizza.objects.order_by('date_added')
    context = {'names' : names}
    return render(request, 'pizzas/names.html', context)

def name(request, name_id):
    """显示某一个披萨及其配料"""
    name = Pizza.objects.get(id=name_id)
    topps = name.topping_set.order_by('date_added')
    context = {'name' : name, 'topps' : topps}
    return render(request, 'pizzas/name.html', context)