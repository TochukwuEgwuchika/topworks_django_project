from django.shortcuts import render

# Create your views here.

def academy(request):
    return render(request, "academy/index.html")
