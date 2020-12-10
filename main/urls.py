from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.main, name='home'),
    path('courses/', views.courses, name='courses'),
    path('news/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.log, name='log'),
    # path('login/', views.UserForm.as_view(), name='my_form'),
    path('success/', views.success, name='success'),
    path('info/', views.page_info, name='info'),
    path('mail', views.ContactPageView.as_view(), name='mail_url'),
    path('<int:pk>', views.FooterCategory.as_view(), name='course_detail'),
    path('<slug:slug>', views.CourseCategory.as_view(), name='course_cat'),
    path('category/<slug:slug>', views.FeaturedDetail.as_view(), name='f_course'),
    path('news/<slug:slug>', views.NewsDetail.as_view(), name='news_detail')

]
