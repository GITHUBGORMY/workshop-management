from urllib import response

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.db.models import customer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control


from workshopApp.forms import managerForm
from workshopApp.forms import workerForm
from workshopApp.models import Login
from django.contrib.auth import logout


# def fun(request):
#     return HttpResponse("Hello")
def fun(request):
    return render(request,'home/Modified_files/index.html')


# @login_required(login_url='/login_view/')
# response["Cache-Control"] = "no-cache, no-store, must-revalidate"
# response["Pragma"] = "no-cache"
# response["Expires"] = "0"
def signin(request):
    return render(request, 'Modified_files/login.html')
def signup(request):
    return render(request, 'Modified_files/register.html')


def home(request):
    return render(request, 'home/Modified_files/index.html')
def dash(request):
    return render(request, 'dash/Modified_files/index.html')
def log(request):
    return render(request, 'Modified_files/login.html')
def reg(request):
    return render(request, 'reg/Modified_files/index.html')
def registration(request):
    return render(request, 'Modified_files/beforeregister.html')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def login_view(request):

        if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('pass')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('admindash')
                elif user.is_worker:
                    return redirect('workerdash')
                elif user.is_customer:
                    return redirect('customerdash')
            else:
                messages.info(request,'invalid credentials')
        return render(request,'Modified_files/login.html')




def worker_register(request):
    worker_Form = workerForm()
    if request.method == 'POST':
        worker_Form = workerForm(request.POST,request.FILES)
        if worker_Form.is_valid():
            user=worker_Form.save(commit=False)
            user.is_worker =True
            user.save()
            worker = worker_Form.save(commit=False)
            worker.user = user
            worker.save()
            # storage = messages.get_messages(request)
            # storage.used = True
            # list(messages.get_messages(request))
            messages.success(request, 'registration successfully complete')
            return redirect('workerdash', message='Save complete')
    return render(request,'Modified_files/register.html',{'worker_form': worker_Form}, )
def messages(request):
    return render(request, 'Modified_files/messages.html')
#
def manager_register(request):
    manager_Form = managerForm()
    if request.method == 'POST':
        manager_Form = managerForm(request.POST,request.FILES)
        if  manager_Form.is_valid():
            user=manager_Form.save(commit=False)
            user.is_customer =True
            user.save()
            manager = manager_Form.save(commit=False)
            manager.user = user
            manager.save()
            messages.info(request,'registration successfully complete')
            return redirect("customerdash")
    return render(request,'Modified_files/register.html',{'manager_Form': manager_Form})
# def view(request):
#     data = Login.objects.all()
#     return render(request,'register/view.html',{"data":data})

#
@login_required
def work_view(request):
    data = Login.objects.filter(is_worker=True)
    return render(request,'Admintemp/worker_view.html',{"data":data})
@login_required
def accept_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("work_view")
@login_required
def reject_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("work_view")
#
@login_required
def customer_view(request):
    data =Login.objects.filter(is_customer=True)
    return render(request,'Admintemp/customer_view.html',{"data":data})
#
#
@login_required
def worker_delete(request,id):
    data =Login .objects.get(id=id)
    data.delete()
    return redirect('work_view')
@login_required
def worker_update(request,id):
    work = Login.objects.get(id=id)
    form = workerForm(instance=work)
    if request.method == 'POST':
        form = workerForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('work_view')
    return render(request,'worker/update.html',{'form':form})
@login_required
def manager_delete(request,id):
    data =Login .objects.get(id=id)
    data.delete()
    return redirect('manager_view')
@login_required
def manager_update(request,id):
    manage = Login.objects.get(id=id)
    form = managerForm(instance=manage)
    if request.method == 'POST':
        form = managerForm(request.POST,instance=manage)
        if form.is_valid():
            form.save()
            return redirect('manager_view')
    return render(request,'customer/update.html',{'form':form})
#
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required
def logout_view(request):
    logout(request)
    # return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))
    return redirect('home')
#

# def category_register(request):
#     category_form = WorkerCategoryForm()
#     data = category.objects.all()
#     if request.method == 'POST':
#         category_form = WorkerCategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('category_register')
#     return render(request, 'Admintemp/categories.html', {'category': category_form, 'data': data})