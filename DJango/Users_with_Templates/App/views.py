from django.shortcuts import render, redirect


from App.models import A
def index(request):
    context = {
    	"all_users": A.objects.all()
    }
    return render(request, "index.html", context)
def add(request):
    firstt=request.POST['one']
    last=request.POST['two']
    email1=request.POST['three']
    age1=int(request.POST['four'])
    A.objects.create(first_name=firstt,last_name=last,email_adress=email1,age=age1)
    return redirect("/")
    