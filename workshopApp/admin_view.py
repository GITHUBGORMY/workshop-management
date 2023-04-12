from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from workshopApp.forms import feedbackForm, WorkerCategoryForm, ScheduleForm
from workshopApp.forms import workerForm
from workshopApp.models import feedback, category, schedule


def admindash(request):
    return render(request, 'Admintemp/index.html')

def feedbacks(request):
    u = request.user
    data = feedback.objects.all()
    return render(request, 'Admintemp/feedbacks.html', {'data': data})


def reply_feedback(request, id):
    Feedback = feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        Feedback.reply = r
        Feedback.save()
        messages.info(request, 'Reply send')
        return redirect('feedbacks')
    return render(request, 'Admintemp/reply_feedbacks.html', {'Feedback': Feedback})

def category_register(request):
    category_form = WorkerCategoryForm()
    data = category.objects.all()
    if request.method == 'POST':
        category_form = WorkerCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_register')
    return render(request, 'Admintemp/categories.html', {'category': category_form, 'data': data})


def category_view(request):
    u = request.user
    data = category.objects.all()
    return render(request, 'Admintemp/category view.html', {'data': data})


def Schedule(request):
    Schedule_form = ScheduleForm()
    data = schedule.objects.all()
    if request.method == 'POST':
        Schedule_form = ScheduleForm(request.POST)
        if Schedule_form.is_valid():
            Schedule_form.save()
            return redirect('Schedule')
    return render(request, 'Admintemp/schedule.html', {'schedule': Schedule_form, 'data': data})