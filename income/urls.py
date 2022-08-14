from django.urls import path
from . import views


urlpatterns = [
    path('', views.IncomeListAPIView.as_view(), name='income sources'),
    path('<int:id>', views.IncomeDetailAPIView.as_view(), name='income details'),
]