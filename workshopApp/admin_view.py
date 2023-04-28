from django.contrib import messages
from django.shortcuts import render, redirect


from workshopApp.forms import WorkerCategoryForm, PaymentForm
from workshopApp.models import feedback, category, schedule, Login, Payment, Appointment


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

def schedule_view(request):
    data = schedule.objects.all()
    return render(request, 'Admintemp/schedule_view.html', {"data": data})

def accept_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("worker_view")

def reject_worker(request,id):
    data = Login.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("worker_view")
def payment_view(request):
    data = Payment.objects.all()
    return render(request, 'Admintemp/payment_view.html', {"data": data})
def approve_payment(request,id):
    data = Payment.objects.get(id=id)
    data.status=1
    data.save()
    return redirect("payment_view")

def reject_payment(request,id):
    data = Payment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("payment_view")

def payment(request):
    data = Appointment.objects.all()
    return render(request, 'Admintemp/appointment.html', {'data': data})
def bill(request):
    data = Payment.objects.all()
    return render(request, 'Admintemp/payment_view.html', {"data": data})

def Generate_bill(request,id):
    payment_form = PaymentForm()
    data =Payment.objects.all()
    if request.method == 'POST':
            payment_form = PaymentForm(request.POST)
            if payment_form.is_valid():
                payment_form.save()
                return redirect('bill')
    return render(request, 'Admintemp/bill.html', {'payment': payment_form ,"data": data})

def bill_update(request,id):
    pay = Payment.objects.get(id=id)
    form = PaymentForm(instance=pay)
    if request.method == 'POST':
        form = PaymentForm(request.POST,instance=pay)
        if form.is_valid():
            form.save()
            return redirect('bill')
    return render(request,'Admintemp/bill_update.html',{'form':form})