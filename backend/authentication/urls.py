from django.urls import path
from . import views

urlpatterns = [
    path("auth/register", views.register, name="register"),
    path("auth/login", views.login_user, name="login_user"),
    path("income/add", views.add_income, name="add_income"),
    path("income/get", views.get_income, name="get_income"),
    path("expense/add", views.add_expense, name="add_expense"),
    path("expense/get", views.get_expense, name="get_expense"),
    path("summary/get", views.get_summary, name='get_summary')
]