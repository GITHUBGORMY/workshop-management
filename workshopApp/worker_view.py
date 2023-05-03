from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from workshopApp.forms import feedbackForm, ScheduleForm, PaymentForm
from workshopApp.models import feedback, Login, schedule, Appointment

@login_required
def workerdash(request):
    return render(request, 'worker/worker_base.html')
@login_required
def work(request):
    data = Login.objects.filter(is_worker=True)
    return render(request,'worker/worker_view.html',{"data":data})

@login_required
def schedule_fun(request):
    schedule_form = ScheduleForm()
    u = request.user
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            obj=schedule_form.save()
            obj.worker = u
            obj.save()
            messages.info(request, 'registration successfully complete')
            return redirect('scheduleview')
    return render(request, 'worker/schedule.html', {'schedule': schedule_form})
@login_required
def scheduleview(request):
    data = schedule.objects.all()
    return render(request, 'worker/schedule_view.html', {"data": data})
@login_required
def schedule_delete(request,id):
    data = schedule.objects.get(id=id)
    data.delete()
    return redirect('scheduleview')
@login_required
def schedule_update(request,id):
    sche = schedule.objects.get(id=id)
    form = ScheduleForm(instance=sche)
    if request.method == 'POST':
        form = ScheduleForm(request.POST,instance=sche)
        if form.is_valid():
            form.save()
            return redirect('scheduleview')
    return render(request,'worker/schedule_update.html',{'form':form})
@login_required
def booked_app(request):
    data = Appointment.objects.all()
    return render(request,'worker/booking_worker.html',{'data': data})
@login_required
def approve_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("booked_app")
@login_required
def reject_booking(request,id):
    data = Appointment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("booked_app")
@login_required
def workdone(request,id):
    data = Appointment.objects.get(id=id)
    data.done=1
    data.save()
    return redirect("booked_app")
#
@login_required
def notdone(request,id):
    data = Appointment.objects.get(id=id)
    data.done=2
    data.save()
    return redirect("booked_app")

@login_required
def Paymentfun(request):
    payment_form = PaymentForm()
    u = request.user
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            obj=payment_form.save()
            obj.user = u
            obj.save()
            messages.info(request, 'successfully complete')
            return redirect('Paymentfun')
    return render(request, 'worker/payment.html', {'payment': payment_form})

