from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.customer_form, name='employee_insert'),
    path('list/', views.customer_list, name='employee_list'),
    path('<int:id>/', views.customer_form, name='customer_update'),
    path('delete/', views.customer_delete),
    path('toggle-finished/<int:id>/', views.toggle_order_finished, name='toggle_order_finished'),
]