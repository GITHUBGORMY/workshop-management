from django.contrib import messages
from django.shortcuts import render, redirect


from workshopApp.forms import feedbackForm, ScheduleForm, PaymentForm
from workshopApp.models import feedback, Login, schedule, Appointment


def workerdash(request):
    return render(request, 'worker/worker_base.html')
def work(request):
    data = Login.objects.filter(is_worker=True)
    return render(request,'worker/worker_view.html',{"data":data})

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

    return render(request, 'worker/feedback.html', {'feedback_form': feedback_form})
def feedback_view(request):
    u=request.user
    data = feedback.objects.filter(user=u)
    return render(request, 'worker/feedback_view.html', {"data": data})

def schedule_fun(request):
    schedule_form = ScheduleForm()
    u = request.user
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            obj=schedule_form.save()
            obj.user = u
            obj.save()
            messages.info(request, 'registration successfully complete')
            return redirect('scheduleview')
    return render(request, 'worker/schedule.html', {'schedule': schedule_form})
def scheduleview(request):
    data = schedule.objects.all()
    return render(request, 'worker/schedule_view.html', {"data": data})
def schedule_delete(request,id):
    data = schedule.objects.get(id=id)
    data.delete()
    return redirect('scheduleview')
def schedule_update(request,id):
    sche = schedule.objects.get(id=id)
    form = ScheduleForm(instance=sche)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=sche)
        if form.is_valid():
            form.save()
            return redirect('scheduleview')
    return render(request,'worker/schedule_update.html',{'form':form})
def booked_app(request):
    data = Appointment.objects.all()
    return render(request,'worker/booking_worker.html',{'data': data})

def approve_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("booked_app")

def reject_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("booked_app")

def Paymentfun(request):
    payment_form = PaymentForm()
    u = request.user
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            obj=payment_form.save()
            obj.user = u
            obj.save()
            messages.info(request, 'registration successfully complete')
            return redirect('Paymentfun')
    return render(request, 'worker/payment.html', {'payment': payment_form})