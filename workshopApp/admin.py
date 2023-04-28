from django.contrib import admin

# Register your models here.
from workshopApp import models

admin.site.register(models.Login)
# admin.site.register(models.worker)
# admin.site.register(models.customer)
admin.site.register(models.feedback)
admin.site.register(models.category)
admin.site.register(models.schedule)
admin.site.register(models.Appointment)
admin.site.register(models.Payment)
admin.site.register(models.bill)



# Register your models here.

