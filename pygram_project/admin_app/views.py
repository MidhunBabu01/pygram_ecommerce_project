from django.shortcuts import redirect, render
# from admin_app.models import AdminProducts
from .forms import AdminProductsForms
from django.contrib import messages
from fashion_hub_app.models import Products
# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Midhun' and password == '123':
            return redirect("admin_app:admin_home")
        else:
            return redirect("admin_app:admin_login")    
    return render(request,"adminlogin.html")



def admin_home(request):
    if request.method == 'POST':
        form = AdminProductsForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AdminProductsForms()

    products = Products.objects.all()
    return render(request,"admin_home.html",{'form':form,'products':products})


def delete(request,item_id):
    if request.method == 'POST':
        item = Products.objects.filter(id=item_id)
        item.delete()
        return redirect('admin_app:admin_home')


def update(request,item_id):
    if request.method == 'POST':
        update  = Products.objects.get(id=item_id)
        fm = AdminProductsForms(request.POST,instance=update)
        if fm.is_valid():
            fm.save()
            return redirect("admin_app:admin_home")
    else:
        update  = Products.objects.get(id=item_id)
        fm = AdminProductsForms(instance=update)
    return render(request,"admin_update.html",{'form':fm})
