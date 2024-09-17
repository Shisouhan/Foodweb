from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def food1(request):
    return render(request, 'food1.html')

def food2(request):
    return render(request, 'food2.html')

def food3(request):
    return render(request, 'food3.html')

def about(request):
    return render(request, 'about.html')