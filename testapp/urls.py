from testapp import views
from django.conf.urls import url
from django.urls import path
urlpatterns=[
 url('about/',views.about),
 url('contact/',views.contact),
 url('^$',views.greeting),
 url('employee/',views.employee_info_view)

]
