from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from .views import user_login, user_logout, dashboard

urlpatterns = [
    path('',views.index,name='index'),
    path('memberedit/<int:id>',views.memberedit,name='memberedit'),
    path('blog/',views.blog,name='blog'),
    # path('blog/blog-details/',views.blog_details,name='blog_details'),
    path('sermon/sermon-details/<int:id>',views.sermon,name='sermon'),
    # path('sermon/sermon-details/<int:id>,views.sermon,name='sermon'),
    # path('events/GHAG-Events',views.events,name='events'),
    path('events',views.events,name='events'),
    path('joinUs',views.member,name='member'),
    path("register/", views.register_member, name="register_member"), 
    path('base',views.base,name='base'),
    # path('login',views.login,name='login'),
    path('childrens-ministries',views.child,name='child'),
    path('youths-ministries',views.youth,name='youth'),
    path('mens-ministries',views.men,name='men'),
    path('womens-ministries',views.women,name='women'),
    path('sports-ministries',views.sport,name='sport'),
    path('sermons_details',views.sermon_details,name='sermons_details'),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path('signup',views.signup,name='signup'),
    path('certifiacate',views.certificate,name='certificate')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)