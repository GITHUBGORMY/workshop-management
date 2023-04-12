from django.urls import path

from workshopApp import views, customer_view, admin_view, manager_view

urlpatterns=[
    path('',views.fun,name='fun'),
    # path('temp', views.temp, name='temp'),
    path('registration', views.registration, name='registration'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('dash', views.dash, name='dash'),
    path('log', views.log, name='log'),
    path('login_view', views.login_view, name='login_view'),
    path('worker_register', views.worker_register, name='worker_register'),
    path('manager_register', views.manager_register, name='manager_register'),
    path('view', views.view, name='view'),
    path('logout_view', views.logout_view, name='logout_view'),

 #admin
    path('admindash', admin_view.admindash, name='admindash'),

    path('work_view', views.work_view, name='work_view'),
    path('manager_view', views.manager_view, name='manager_view'),
    path('worker_delete/<int:id>/',views.worker_delete,name='worker_delete'),
    path('worker_update/<int:id>/',views.worker_update,name='worker_update'),
    path('manager_delete/<int:id>/',views.manager_delete,name='manager_delete'),
    path('manager_update/<int:id>/',views.manager_update,name='manager_update'),
    path('feedbacks', admin_view.feedbacks, name='feedbacks'),
    path('category_view', admin_view.category_view, name='category_view'),
    path('category_register', admin_view.category_register, name='category_register'),
    path('reply_feedback/<int:id>/', admin_view.reply_feedback, name='reply_feedback'),



#customer
   path('customerdash', customer_view.customerdash, name='customerdash'),
   path('work', customer_view.work, name='work'),
   path('feedbak_register', customer_view.feedbak_register, name='feedbak_register'),
   path('feedback_view', customer_view.feedback_view, name='feedback_view'),

#manager
   path('managerdash', manager_view.managerdash, name='managerdash'),
   path('manage_view', manager_view.manage_view, name='manage_view'),



]