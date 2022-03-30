import datetime
import random
from django.shortcuts import render, redirect


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['messages'] = []
    context = {'gold': request.session['gold'], 'messages': request.session['messages']}
    return render(request, 'index.html', context)

    

def process_money(request):
    if request.method == "POST":
        directory = {'farm': [10,20],'cave': [5,10],'house': [2,5],'casino': [-50,50]}
        now = datetime.datetime.now()

        for key in directory:
            if key == request.POST['which_form']:
                temp = random.randint(directory[key][0], directory[key][1])
                request.session['gold'] += temp
                if temp >= 0:
                    request.session['messages'].insert(0,'Earned '+ str(temp) + ' golds from the ' + key + '! ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
                else:
                    request.session['messages'].insert(0,'Entered a ' + key + ' and lost '+ str(temp*-1) + ' golds... Ouch.. ('+now.strftime("%Y/%m/%d %I:%M %p")+')')
    return redirect("/")
