import re

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.forms import forms

from workshopApp.models import Login, feedback, category, schedule, Appointment, Payment, bill
from django import forms
#



EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class DateInput(forms.DateInput):
    input_type = 'date'

class Timeinput(forms.TimeInput):
    input_type = 'time'

email = forms.CharField(validators=
                        [RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" ,message='please enter v email')])

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('Please enter a valid phone number')

class workerForm(UserCreationForm):
    phone = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model= Login
        fields = ('name','phone','email','address','profilepicture','category','username','password1','password2')

        #
        # def clean_phone_no(self):
        #     phone = self.cleaned_data.get('phone', None)
        #     try:
        #         int(phone)
        #     except (ValueError, TypeError):
        #         raise ValidationError('Please enter a valid phone number')
        #     return phone
        # def clean_email(self):
        #     email = self.cleaned_data.get('email')
        #     if email and not re.match(EMAIL_REGEX, email):
        #         raise forms.ValidationError('Invalid email format')
        #     return email

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('@gmail'):
    #         raise forms.ValidationError("Only @gmail email addresses allowed")
    #     return email

class managerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('name', 'phone', 'email','address', 'profilepicture', 'category', 'username', 'password1', 'password2')

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ('message',)
        # exclude = ("worker","reply")

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
        fields = ('description','date','amount')
class BillForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=DateInput)
    class Meta:
        model = bill
        fields = ('card_num','expiry_date','cvv')




# class LoginRegister(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
#
#     class Meta:
#         model = Login
#         fields = ('username', 'password1', 'password2')





