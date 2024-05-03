from django.urls import path
from . import views


urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog_comment_list/', views.blogcomment_list, name='blogcomment_list'),
    path('blog_comment_detail/<int:pk>/', views.blogcomment_detail,  name='blogcomment_detail'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact_detail/<int:pk>/', views.contact_detail, name='contact_detail'),
]
