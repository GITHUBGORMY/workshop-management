from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from workshopApp.forms import WorkerCategoryForm, PaymentForm
from workshopApp.models import feedback, category, schedule, Login, Payment, Appointment

@login_required
def admindash(request):
    return render(request, 'Admintemp/index.html')
@login_required
def feedbacks(request):
    u = request.user
    data = feedback.objects.all()
    return render(request, 'Admintemp/feedbacks.html', {'data': data})

@login_required
def reply_feedback(request, id):
    Feedback = feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        Feedback.reply = r
        Feedback.save()
        messages.info(request, 'Reply send')
        return redirect('feedbacks')
    return render(request, 'Admintemp/reply_feedbacks.html', {'Feedback': Feedback})
@login_required
def category_register(request):
    category_form = WorkerCategoryForm()
    data = category.objects.all()
    if request.method == 'POST':
        category_form = WorkerCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_register')
    return render(request, 'Admintemp/categories.html', {'category': category_form, 'data': data})

@login_required
def category_view(request):
    u = request.user
    data = category.objects.all()
    return render(request, 'Admintemp/category view.html', {'data': data})
@login_required
def schedule_view(request):
    data = schedule.objects.all()
    return render(request, 'Admintemp/schedule_view.html', {"data": data})


def payment_view(request):
    data = Payment.objects.all()
    return render(request, 'Admintemp/payment_view.html', {"data": data})


@login_required
def billgerated(request,id):
    data = Payment.objects.get(id=id)
    data.status=2
    data.save()
    return redirect("payment_view")
@login_required
def payment(request):
    data = Appointment.objects.all()
    return render(request, 'Admintemp/appointment.html', {'data': data})
# def bill(request):
#     data = Payment.objects.all()
#     return render(request, 'Admintemp/payment_view.html', {"data": data})
@login_required
def Generate_bill(request,id):
    payment_form = PaymentForm()
    appoint = Appointment.objects.get(id=id)
    data = Payment.objects.filter(appoint=appoint)
    if data.exists():
        messages.info(request, "You have already exist  ")
        return redirect('schedule_view')
    if request.method == 'POST':
            payment_form = PaymentForm(request.POST)
            if payment_form.is_valid():
                payment_form.save()
                return redirect('payment')
    return render(request, 'Admintemp/bill.html', {'payment': payment_form})

# def bill_update(request,id):
#     pay = Payment.objects.get(id=id)
#     form = PaymentForm(instance=pay)
#     if request.method == 'POST':
#         form = PaymentForm(request.POST,instance=pay)
#         if form.is_valid():
#             form.save()
#             return redirect('bill')
#     return render(request,'Admintemp/bill_update.html',{'form':form})