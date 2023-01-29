from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    date=datetime.today()
    return render(request,"index.html",context={"date":date})


