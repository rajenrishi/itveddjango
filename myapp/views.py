from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def show(request):
   text = """<h1>In django app page</h1>"""
   return HttpResponse(text)


def show_count(request, count):
   text = f"""<h1>In django app page: {count}</h1>"""
   return HttpResponse(text)


def show_year(request, year):
   text = f"""<h1>In django app page: {year}</h1>"""
   return HttpResponse(text)
