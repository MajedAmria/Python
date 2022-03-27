
from django.shortcuts import render
def show(request):
    return render(request,"index.html")
def index(request):
    if request.method == "POST":
        name=request.POST["name"]
        location=request.POST["location"]
        language=request.POST["language"]
        context = {
    	"name" : name,
    	"location" : location,
        "language":language
         }
    
    return render(request,"show.html",context)
