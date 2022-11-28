from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)
from django.http import HttpRequest
from employees.models import Employee


# Страница после авторизации
def MeView(request: HttpRequest):
    def group_name(request):
        if request.user.groups.filter(name='workers').exists():
            return 'Рабочий персонал'

        if request.user.groups.filter(name='masters').exists():
            return 'Руководство'

        return 'No'

    parameters = {
        'group_name': group_name(request)
    }

    context = {
        "employee": (
            Employee.objects
            .filter(user_id=request.user.id)
            .order_by('pk').all()
        ),
        "params": (
            parameters)
    }

    return render(request=request, template_name="myauth/me.html", context=context)


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:me")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("myauth:me")
