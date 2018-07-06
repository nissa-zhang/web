from django.shortcuts import render, redirect, get_list_or_404
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from item.models import Item
# from item.forms import SampleForm, InputForm, InputForm2, InputForm3, ItemForm

# Create your views here.
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('welcome')

def doget_execute(request,param1):
    return HttpResponse(param1)

def showtemp1(request):
    c = {
        'key1': 'hello everyone',
    }
    return render(request, 'template1.html', c)

def showtemp1sc(request):
    return render(request, 'template1.html', {'key1': 'hello everyone'})

def showredirect(request):
    return redirect('/show')

def showredirect2(request):
    return redirect('wel')

def showredirect3(request):
    return render(request, 'templateform.html')

def tempif(request):
    context = { 'key1': 'goodmorning'}
    return render(request, 'templateif.html', context)

def tempfor(request):
    context = { 'key1': ['hello','Django','world']}
    return render(request, 'templatefor.html', context)

def showchild(request):
    return render(request, 'child.html')

@csrf_protect
def dopost_execute(request):
    param = request.POST['message']
    return render(request, 'result.html', {'message': param})

def show_input(request):
    return render(request, 'input.html')

def show_inputerr(request):
    return render(request, 'input_tokenerror.html')

def csrf_failure(request, reason=''):
    c = {'message': 'トークンエラー'}
    return render(request, '403_csrf.html', c)

# 演習6-
def view(request):
    # ---- 演習6
    return render(request, 'c_input.html')

# 演習6-
# def execute(request):
#     # ---- 演習6
#     p1 = int(request.GET['p1'])
#     p2 = int(request.GET['p2'])
#     res = p1 + p2
#     return render(request, 'c_result.html', {'res': res})

# 演習7
def csrf_failure(request, reason=''):
    c = {'err_msg': 'tokenError'}
    return render(request,'403_csrf.html', c)

# 演習8

def confirm(request):
    p1 = request.POST['p1']
    request.session['p1'] = p1
    return render(request, 'c_confirm.html')

# 演習8
def execute(request):
    p1 = request.session['p1']
    return render(request, 'c_result.html', {'p1': p1})

def mozaiku(request):
    p1 = request.session['p1']
    request.session['p1'] = p1
    return render(request, 'c_mozaiku.html')
def tamp(request):
    return render(request, 'tamplate.html')

