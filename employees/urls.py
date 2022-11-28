from django.urls import path
from .views import EmployeesListView, EmployeeDetailView, EmployeeDeleteView, EmployeeCreateView, EmployeeUpdateView


app_name = "employees"

urlpatterns = [

    # Список сотрудников
    path("", EmployeesListView.as_view(), name="index"),

    # Карточка сотрудника
    path("<int:pk>", EmployeeDetailView.as_view(), name="details"),

    # Удаление сотрудника
    path("<int:pk>/confirm-delete", EmployeeDeleteView.as_view(), name="delete-employee"),

    # Создание сотрудника
    path("create/", EmployeeCreateView.as_view(), name="create-employee"),

    # Редактирование данных сотрудника
    path("update/<int:pk>", EmployeeUpdateView.as_view(), name="update-employee"),
]