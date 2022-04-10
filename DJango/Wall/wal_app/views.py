from django.shortcuts import render,redirect
from .models import *


def wall(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        context = {
            "all_msgs": Message.objects.all().order_by("created_at")
        }
        return render(request, "wall.html", context)

def post_message(request):
    thisUser = User.objects.get(id=request.session['user_id'])
    Message.objects.create(user=thisUser, message=request.POST['message'])
    return redirect("/wall")

def post_comment(request, msg_id):
    thisUser = User.objects.get(id=request.session['user_id'])
    thisMsg = Message.objects.get(id=msg_id)
    Comment.objects.create(message=thisMsg, user=thisUser, comment=request.POST['cmntText'])
    return redirect("/wall")

def user_posts(request, user_id):
    thisUser = User.objects.get(id=user_id)
    context = {
        "user_messages": thisUser.messages.all(),
        "user_comments": thisUser.comments.all()
    }
    return render(request, "posts.html", context)
    
def sucsses(request):
    if  'email' in request.session :
      user=User.objects.get(email=request.session['email'])
    
      context={
            'firstname': user.first_name
                }
    
      return render(request,"dashbord.html",context) 
    else:
      return redirect('/')
    
def logout(request):
    del request.session['email']
    
    return redirect('/')