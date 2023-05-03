from django.urls import path
from django.conf import settings
from workshopApp import views, worker_view, admin_view, customer_view
from django.contrib.auth import views as auth_views
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
    # path('view', views.view, name='view'),
    # path('logout_view', views.logout_view,{'home': settings.LOGOUT_REDIRECT_URL},name='logout_view'),
    path('logout_view', auth_views.LogoutView.as_view(next_page='home'),name='logout_view'),
    # path('logout_view/', views.logout_view, name='logout_view'),
    path('messages', views.messages, name='messages'),

 #admin
    path('admindash', admin_view.admindash, name='admindash'),

    path('work_view', views.work_view, name='work_view'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('worker_delete/<int:id>/',views.worker_delete,name='worker_delete'),
    path('worker_update/<int:id>/',views.worker_update,name='worker_update'),
    path('manager_delete/<int:id>/',views.manager_delete,name='manager_delete'),
    path('manager_update/<int:id>/',views.manager_update,name='manager_update'),
    path('feedbacks', admin_view.feedbacks, name='feedbacks'),
    path('category_view', admin_view.category_view, name='category_view'),
    path('category_register', admin_view.category_register, name='category_register'),

    path('reply_feedback/<int:id>/', admin_view.reply_feedback, name='reply_feedback'),
    path('schedule_view', admin_view.schedule_view, name='schedule_view'),
    path('accept_worker/<int:id>/', views.accept_worker, name='accept_worker'),
    path('reject_worker/<int:id>/', views.reject_worker, name='reject_worker'),
    path('payment', admin_view.payment, name='payment'),
    path('billgerated/<int:id>/', admin_view.billgerated, name='billgerated'),
    # path('reject_payment/<int:id>/', admin_view.reject_payment, name='reject_payment'),
    # path('bill', admin_view.bill, name='bill'),
    # path('bill_update/<int:id>/', admin_view.bill_update, name='bill_update'),
    path('Generate_bill/<int:id>/', admin_view.Generate_bill, name='Generate_bill'),


#worker
   path('workerdash', worker_view.workerdash, name='workerdash'),
   path('work', worker_view.work, name='work'),
   path('scheduleview', worker_view.scheduleview, name='scheduleview'),
   path('schedule_fun', worker_view.schedule_fun, name='schedule_fun'),
   path('schedule_delete/<int:id>/', worker_view.schedule_delete, name='schedule_delete'),
   path('schedule_update/<int:id>/', worker_view.schedule_update, name='schedule_update'),
   path('booked_app', worker_view.booked_app, name='booked_app'),
   path('approve_booking/<int:id>/', worker_view.approve_booking, name='approve_booking'),
   path('reject_booking/<int:id>/', worker_view.reject_booking, name='reject_booking'),
   path('workdone/<int:id>/', worker_view.workdone, name='workdone'),
   path('notdone/<int:id>/', worker_view.notdone, name='notdone'),
   path('Paymentfun', worker_view.Paymentfun, name='Paymentfun'),
 #customer
   path('customerdash', customer_view.customerdash, name='customerdash'),
   path('manage_view', customer_view.manage_view, name='manage_view'),
   path('schedule_viewcu', customer_view.schedule_viewcu, name='schedule_viewcu'),
   path('book_appointment/<int:id>/', customer_view.book_appointment, name='book_appointment'),
   path('booking', customer_view.booking, name='booking'),
   path('feedbak_register', customer_view.feedbak_register, name='feedbak_register'),
   path('feedback_view', customer_view.feedback_view, name='feedback_view'),
   path('customer_bookings_view', customer_view.customer_bookings_view, name='customer_bookings_view'),
   path('payment_view', customer_view.payment_view, name='payment_view'),
   path('beforebill', customer_view.beforebill, name='beforebill'),
   path('onlinepayment/<int:id>/', customer_view.onlinepayment, name='onlinepayment'),
   path('approve_payment/<int:id>/', customer_view.approve_payment, name='approve_payment'),


]