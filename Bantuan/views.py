from django.shortcuts import render

# Create your views here.

def web1(request):
    return render(request, 'index1.html')