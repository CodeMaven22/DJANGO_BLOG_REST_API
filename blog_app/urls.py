from django.urls import path
from . import views


urlpatterns = [
    path('create_blog/', views.create_blog,  name='create_blog'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog_update/<int:pk>/', views.blog_update, name='blog_update'),
    path('blog_delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    
    path('create_comment/', views.create_comment,  name='create-comment'),
    path('blog_comment_list/', views.blogcomment_list, name='blogcomment_list'),
    path('blog_comment_detail/<int:pk>/', views.blogcomment_detail,  name='blogcomment_detail'),
    path('blogcomment_update/<int:pk>/', views.blockcomment_update, name='blogcomment-update'),
    path('blogcomment_delete/<int:pk>/', views.blockcomment_delete, name='blockcomment-delete'),
    
    path('create_contact/', views.create_contact, name='create-contact'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact_detail/<int:pk>/', views.contact_detail, name='contact-detail'),
    path('contact_update/<int:pk>/', views.contact_update, name='contact-update'),
    path('contact_delete/<int:pk>/', views.contact_delete, name='contact-delete'),
]
