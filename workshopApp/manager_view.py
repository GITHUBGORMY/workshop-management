from django.shortcuts import render

from workshopApp.models import Login


def manage_view(request):
    data =Login.objects.filter(is_manager=True)
    return render(request,'manager/manager_view.html',{"data":data})
def managerdash(request):
    return render(request,'manager/managerbase.html')