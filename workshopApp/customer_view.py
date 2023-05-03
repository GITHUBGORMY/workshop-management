from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from workshopApp.forms import BillForm, feedbackForm
from workshopApp.models import Login, schedule, Appointment, Payment, bill, feedback


@login_required
def manage_view(request):
    data =Login.objects.filter(is_customer=True)
    return render(request,'customer/work_view.html',{"data":data})
@login_required
def customerdash(request):
    return render(request,'customer/customerbase.html')
@login_required
def schedule_viewcu(request):
    u=request.user
    data = schedule.objects.all()
    return render(request, 'customer/schedule_view.html', {"data": data})
@login_required
def book_appointment(request,id):
    Schedule = schedule.objects.get(id=id)
    worker = Login.objects.get(name=request.user)
    data = Appointment.objects.filter(worker=worker,schedule=Schedule)
    if data.exists():
        messages.info(request,"You have already requested ")
        return redirect('booking')
    else:
        if request.method == 'POST':
                obj = Appointment()
                obj.worker = worker
                obj.schedule = Schedule
                obj.save()
                messages.info(request,'Appointment Booked ')
                return redirect('customer_bookings_view')
    return render(request,'customer/booking.html',{'schedule':Schedule})
# def booking(request):
#     data = schedule.objects.filter(is_worker=True)
#     return render(request,'customer/customerschedule.html',{'data':data})
@login_required
def booking(request):
    data = schedule.objects.all()
    return render(request, 'customer/cuschedule.html', {"data": data})
@login_required
def customer_bookings_view(request):
    worker = Login.objects.get(name=request.user)
    appointments = Appointment.objects.filter(worker=worker)
    # appointments = Appointment.objects.all()
    return render(request, 'customer/booking_history.html', {'appointments': appointments})
@login_required
def payment_view(request):
    u = request.user
    data = Payment.objects.all()
    return render(request, 'customer/payment.html', {"data": data})
@login_required
def beforebill(request):
    return render(request,'customer/selectpay.html')
@login_required
def onlinepayment(request,id):
    bill_form = BillForm()
    payment = Payment.objects.get(id=id)
    if request.method == 'POST':
            bill_form = BillForm(request.POST)
            if bill_form.is_valid():
                bill_form.save()
                return redirect('payment_view')
    return render(request, 'customer/online.html', {'bill': bill_form})
@login_required
def approve_payment(request,id):
    data = Payment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("payment")
@login_required
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
@login_required
def feedback_view(request):
    u=request.user
    data = feedback.objects.all()
    return render(request, 'customer/feedback_view.html', {"data": data})