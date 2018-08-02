from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('account/logout/', views.Logout),
    path('new', views.new, name='new_client'),
    path('create', views.create, name='create_client'),
    re_path(r'^show/(?P<id>\d+$)', views.show, name='show_client'),
    re_path(r'^edit/(?P<id>\d+$)',views.edit, name='edit_client'),
    re_path(r'^update$',views.update, name='update_client'),
    re_path(r'^delete/(?P<id>\d+$)',views.delete, name='delete')
]
