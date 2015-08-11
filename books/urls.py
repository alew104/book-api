from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'books/$', views.BookList.as_view(), name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
