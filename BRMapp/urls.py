from BRMapp import views
from django.conf.urls import url
urlpatterns=[
 url('view-books',views.viewBooks),
 url('edit-book',views.editBook),
 url('search-book',views.searchBook),
 url('new-book',views.newBook),
 url('delete-book',views.deleteBook),
 url(r'^add',views.add),  #r-means regular expression. ^ means startswith. $ means endswith
 url('search',views.search),
 url('edit',views.edit),
 url('login',views.userLogin),
 url('logout',views.userlogout),
]
