from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderApiView.as_view()),
    path('orders/<int:pk>/', views.SingleOrderView.as_view()),
    path('workers/', views.WorkerApiView.as_view()),
    path('workers/<int:pk>/', views.SingleWorkerView.as_view()),
    path('job/', views.WorkerJobApiView.as_view()),
    path('job/<int:pk>/', views.SingleWorkerJobView.as_view()),
]