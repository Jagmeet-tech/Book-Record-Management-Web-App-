from exam import views
from django.conf.urls import url
urlpatterns=[
 url('test/',views.showtest),
 url('result/',views.showresult)

]
