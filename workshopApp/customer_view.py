from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


from workshopApp.forms import feedbackForm
from workshopApp.forms import workerForm
from workshopApp.models import feedback, Login


def customerdash(request):
    return render(request, 'customer/customer_base.html')
def work(request):
    data = Login.objects.filter(is_worker=True)
    return render(request,'customer/customer_view.html',{"data":data})

def feedbak_register(request):
    feedback_form = feedbackForm()
    u = request.user
    if request.method == 'POST':
        feedback_form =feedbackForm(request.POST,)
        if feedback_form.is_valid():
            obj=feedback_form.save(commit=False)
            obj.user =u
            obj.save()
            messages.info(request, 'registration successfully complete')
            return redirect("feedback_view")
        else:
            feedback_form =feedbackForm()

    return render(request, 'customer/feedback.html', {'feedback_form': feedback_form})
def feedback_view(request):
    u=request.user
    data = feedback.objects.filter(user=u)
    return render(request, 'customer/feedback_view.html', {"data": data})