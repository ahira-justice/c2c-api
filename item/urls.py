from django.urls import path
from item import views


app_name = 'item'


urlpatterns = [
    path('', views.Items.as_view(), name='collection'),
    path('<uuid:pk>/', views.ItemDetail.as_view(), name='resource'),
    path('interest/', views.ShowInterest.as_view(), name='interest'),
    path('marksold/', views.MarkAsSold.as_view(), name='marksold'),
]
