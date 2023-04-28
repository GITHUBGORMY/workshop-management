from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from workshopApp.models import Login, feedback, category, schedule, Appointment, Payment
from django import forms
#
class DateInput(forms.DateInput):
    input_type = 'date'

class Timeinput(forms.TimeInput):
    input_type = 'time'

class workerForm(UserCreationForm):
    class Meta:
        model= Login
        fields = ('name','phone','email','address','profilepicture','category','username','password1','password2')

class managerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('name', 'phone', 'email','address', 'profilepicture', 'category', 'username', 'password1', 'password2')

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ('message','reply')
        exclude = ("user","reply")

class WorkerCategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ("title", "description", )

class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=Timeinput)
    end_time = forms.TimeField(widget=Timeinput)
    class Meta:
        model = schedule
        fields = ('date','start_time','end_time')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('worker','schedule','status')
class PaymentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = ('description','status','date','amount')




# class LoginRegister(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
#
#     class Meta:
#         model = Login
#         fields = ('username', 'password1', 'password2')





