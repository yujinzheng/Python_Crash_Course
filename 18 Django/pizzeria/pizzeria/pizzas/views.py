from django.shortcuts import render

def index(request):
    """pizzas的主页"""
    return render(request, 'pizzas/index.html')