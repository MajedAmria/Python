import random 	
from django.shortcuts import render,redirect


def show(request):
    if  'random' not in request.session:
        request.session['random'] = random.randint(1, 100)
        request.session['status'] = 'new'
        request.session['guesses'] = 0
    print('Status This Session:', request.session['status'])
    print('Random Number This Session:', request.session['random'])
    return render(request,"index.html")


def guess(request):
    if request.POST['guess-value']:
        if int(request.POST['guess-value']) > request.session['random']:
            request.session['status'] ='high'
        elif int(request.POST['guess-value']) < request.session['random']:
            request.session['status'] = 'low'
        else:
            request.session['status'] = 'win'
        request.session['guesses'] += 1
        if request.session['status'] != 'win' and request.session['guesses'] >= 5:
            request.session['status'] = 'lose'
    return redirect("/")


def destroy(request):
    request.session.clear()
    print('Session Cleared')
    return redirect("/")