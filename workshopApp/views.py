from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from workshopApp.forms import feedbackForm, WorkerCategoryForm, managerForm
from workshopApp.forms import workerForm
from workshopApp.models import feedback, category, Login


def fun(request):
    return HttpResponse("Hello")

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
                return redirect('customerdash')
            elif user.is_manager:
                return redirect('managerdash')
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
            messages.info(request,'registration successfully complete')
            return redirect("work_view")
    return render(request,'Modified_files/register.html',{'worker_form': worker_Form})
#
def manager_register(request):

    manager_Form = managerForm()
    if request.method == 'POST':
        manager_Form = managerForm(request.POST,request.FILES)
        if  manager_Form.is_valid():
            user=manager_Form.save(commit=False)
            user.is_manager =True
            user.save()
            manager = manager_Form.save(commit=False)
            manager.user = user
            manager.save()
            messages.info(request,'registration successfully complete')
            return redirect("view")
    return render(request,'Modified_files/register.html',{'manager_Form': manager_Form})
def view(request):
    data = manager.objects.all()
    return render(request,'register/view.html',{"data":data})

#
def work_view(request):
    data = Login.objects.filter(is_worker=True)
    return render(request,'Admintemp/customer_view.html',{"data":data})
#
def manager_view(request):
    data =Login.objects.filter(is_manager=True)
    return render(request,'Admintemp/manager_view.html',{"data":data})
#
#
def worker_delete(request,id):
    data =Login .objects.get(id=id)
    data.delete()
    return redirect('work_view')
def worker_update(request,id):
    work = Login.objects.get(id=id)
    form = workerForm(instance=work)
    if request.method == 'POST':
        form = workerForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('work_view')
    return render(request,'customer/update.html',{'form':form})
def manager_delete(request,id):
    data =Login .objects.get(id=id)
    data.delete()
    return redirect('manager_view')
def manager_update(request,id):
    manage = Login.objects.get(id=id)
    form = managerForm(instance=manage)
    if request.method == 'POST':
        form = managerForm(request.POST,instance=manage)
        if form.is_valid():
            form.save()
            return redirect('manager_view')
    return render(request,'manager/update.html',{'form':form})
#
def logout_view(request):
    logout(request)
    return redirect('login_view')
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