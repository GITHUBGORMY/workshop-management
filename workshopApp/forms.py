from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from workshopApp.models import Login, feedback, category, schedule
from django import forms
#
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
        # exclude = ("user","reply")

class WorkerCategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ("title", "description", )

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ('date','start_time','end_time')




# class LoginRegister(UserCreationForm):
#     username = forms.CharField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )
#
#     class Meta:
#         model = Login
#         fields = ('username', 'password1', 'password2')





