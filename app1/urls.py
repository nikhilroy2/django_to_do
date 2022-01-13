from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('delete/<int:id>', views.Delete, name="delete"),
    path('edit/<int:id>', views.Edit, name='edit')
]