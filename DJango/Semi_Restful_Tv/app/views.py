from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Show

def index(request):
    context={
        'shows':Show.objects.all()
    }
    return render(request,'home.html',context)
def addNewShow(request):
    return render(request,'addNew.html')
def insertShow(request):
    errors = Show.objects.basic_validator(request.POST)
      
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
   
    Show.objects.create(title=request.POST['title1'],Network=request.POST['network'],release_Date=request.POST['date'],discription=request.POST['desc'])
    lastShow= Show.objects.last()
    id=str(lastShow.id)
    return redirect('/shows/'+id)
def show(request,Showid):
    x=Show.objects.get(id=Showid)
    context={
        'show':x
    }
    return render(request, 'show.html',context)
def edit(request,showid):
   
    context={
        'show':Show.objects.get(id=showid)
    }
    return render(request,'edit.html',context)
def update(request,showid):
    errors = Show.objects.basic_validator(request.POST)
      
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str (showid)+'/edit')
    x=Show.objects.get(id=showid)
    x.title=request.POST['title1']
    x.Network=request.POST['network']
    x.release_Date=request.POST['date']
    x.discription=request.POST['desc']
    x.save()
    return redirect('/shows')
def delete(request,showid):
    x=Show.objects.get(id=showid)
    x.delete()
    return redirect('/shows')

