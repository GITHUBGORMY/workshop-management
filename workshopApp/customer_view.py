from django.contrib import messages
from django.shortcuts import render, redirect

from workshopApp.models import Login, schedule, Appointment, Payment


def manage_view(request):
    data =Login.objects.filter(is_customer=True)
    return render(request,'customer/work_view.html',{"data":data})
def customerdash(request):
    return render(request,'customer/customerbase.html')
def schedule_viewcu(request):
    u=request.user
    data = schedule.objects.all()
    return render(request, 'customer/schedule_view.html', {"data": data})

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
def booking(request):
    data = schedule.objects.all()
    return render(request, 'customer/cuschedule.html', {"data": data})

def customer_bookings_view(request):
    worker = Login.objects.get(name=request.user)
    appointments = Appointment.objects.filter(worker=worker)
    # appointments = Appointment.objects.all()
    return render(request, 'customer/booking_history.html', {'appointments': appointments})
def payment_view(request):
    u = request.user
    appoint = Appointment.objects.get(worker=request.user)
    data = Payment.objects.filter(appoint=appoint)
    return render(request, 'customer/payment.html', {"data": data})