""" views.py """
from django.shortcuts import render

def index(request):
    """ index """
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)
