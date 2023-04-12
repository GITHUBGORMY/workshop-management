from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.FloatField(max_length=200, null=True)
    profilepicture = models.FileField(upload_to='documents/', null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=0, null=True)


class schedule(models.Model):
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False)


class feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=150)
    reply = models.CharField(max_length=150, null=True, blank=True)

# class manager(models.Model):
#      user = models.ForeignKey(Login, on_delete=models.CASCADE)
#      name= models.CharField(max_length=200)
#      Email = models.EmailField(max_length=200)
#      address = models.CharField(max_length=200)
#      phone = models.FloatField(max_length=200)
#      document = models.FileField(upload_to='documents/')
#
#
#
# class worker(models.Model):
#     user = models.ForeignKey(Login,on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     Email = models.EmailField(max_length=200)
#     address = models.CharField(max_length=200)
#     phone = models.FloatField(max_length=200)
#     profilepicture = models.FileField(upload_to='documents/')
