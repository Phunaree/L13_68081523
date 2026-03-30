from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form_page, name='form'), 
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]