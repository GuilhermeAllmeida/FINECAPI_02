from django.urls import path

from reserva import views

app_name = 'reserva'

urlpatterns = [
    path('list/', views.ReservaList.as_view(), name='list'),
    path('create/', views.ReservaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ReservaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ReservaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ReservaDelete.as_view(), name='delete'),

]
