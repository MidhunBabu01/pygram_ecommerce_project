from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http.response import JsonResponse



# Create your views here.
def register(request):
    if "username" in request.session:
        return redirect('fashion_hub_app:index')
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("accounts:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email  already registered")
                return redirect("accounts:register")
            else:
                user = User.objects.create_user(username=username, email=email,
                                        password=password1)
                user.save();
                print("user created")
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
        return JsonResponse(
                {'success':True},
                safe=False
            )
    else:
         return render(request,"register.html")



def login(request):
    if 'username' in request.session:
        return redirect('fashion_hub_app:index')
    elif request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
    else:
        return render(request,"login.html")        
    


def logout(request):
    if 'username' in request.session:
        request.session.flush()
    # auth.logout(request)
    return redirect("fashion_hub_app:index")

    






    
