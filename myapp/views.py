import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import generic


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


# Template
def show_template(request):
    template = loader.get_template('templates_demo/index.html')  # getting our template
    return HttpResponse(template.render())  # rendering the template in HttpResponse


def template_var_demo(request):
    template = loader.get_template('templates_demo/template_var_demo.html')
    data = {
        'name': {'nme': 'Rajendra', 'id': 23, 'misc': ['A', 'B']}
    }
    return HttpResponse(template.render(data))


def template_if_tag_demo(request):
    template = loader.get_template('templates_demo/template_if_tag_demo.html')
    context = {
        'num': 6
    }
    return HttpResponse(template.render(context))


def template_for_tag_demo(request):
    template = loader.get_template('templates_demo/template_for_tag_demo.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana']
    }
    return HttpResponse(template.render(data))


def template_empty_for_tag_demo(request):
    template = loader.get_template('templates_demo/template_empty_for_tag_demo.html')
    data = {
        'fruit_list': []
    }
    return HttpResponse(template.render(data))


def template_cycle_tag_demo(request):
    template = loader.get_template('templates_demo/template_cycle_tag_demo.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana', 'pineapple', 'watermelon', 'grapes']
    }
    return HttpResponse(template.render(data))


def template_inheritance_demo(request):
    template = loader.get_template('templates_demo/template_child.html')
    data = {
        'fruit_list': ['orange', 'apple', 'banana', 'pineapple', 'watermelon', 'grapes']
    }
    return HttpResponse(template.render(data))


def template_comments_demo(request):
    template = loader.get_template('templates_demo/template_comments.html')
    data = {
        'name': {'nme': 'Django', 'id': 23, 'misc': ['A', 'B']}
    }
    return HttpResponse(template.render(data))


# Class based views
class MyAppView(generic.View):
    def get(self, request):
        now = datetime.datetime.now()
        html = "<html><body>It is now {}</body></html>".format(now)
        return HttpResponse(html)


# Page redirection examples
def temporary_page_redirect_url(request):
    return redirect(f"/myapp/template_cycle_tag_demo/")


def temporary_page_redirect_name(request):
    return redirect(f"shw_tpl")


def redirect_path_parameters(request):
    my_count = 8
    return redirect("count", count=my_count)


def permanent_page_redirect(request):
    return redirect(f"shw_tpl", permanent=True)
