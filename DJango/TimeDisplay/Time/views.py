from django.shortcuts import render
from datetime import datetime
    
def time_display(request):
    now = datetime.today()

    context = {
        "date": now.strftime('%b %d,%Y'), 
        "time": now.strftime('%H:%M %p') 
    }
    return render(request,'index.html', context)