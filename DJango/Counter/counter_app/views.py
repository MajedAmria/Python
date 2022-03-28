from http.client import HTTPResponse
from django.shortcuts import render,redirect



def display(request):
    # num = request.POST['name']
    if 'time' in request.session:
        request.session['time'] += 1
    else:
        request.session['time'] = 1
    return render(request,"index.html")
def destroy(request):
    del request.session['time']
    return redirect("/")

def reset():
    return redirect("/clear")
def add_two(request):
    request.session['time'] += 1
    return redirect("/")
