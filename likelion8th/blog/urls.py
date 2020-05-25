from django.contrib import admin
from django.urls import path
from . import views


#1함수 1url
urlpatterns = [
    path('<int:blog_id>',views.detail, name ="detail"),
    path('new',views.new, name="new"),
    path('create', views.create, name = "create"),
    path('edit/<int:blog_id>', views.edit, name = "edit"),#id값을 받는 애는 <int:blog_id> 써줘야함
    path('update/<int:blog_id>', views.update, name = "update"),
    path('delete/<int:blog_id>',views.delete, name = 'delete'),
]
