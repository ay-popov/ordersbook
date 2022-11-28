from django.urls import path
from .views import (OrdersCreateView, eq_page, OrdersByDateListView, MyOrdersListView, OrderCompleteView,
                    EqCreateView, OrdersUpdateView, EqUpdateView)

app_name = "orders"

urlpatterns = [

    # Список нарядов на выбранную дату
    path("", OrdersByDateListView, name="by-date"),

    # Список нарядов "Мои наряды" для рабочего
    path("my_orders/", MyOrdersListView, name="my_orders"),

    # Создание наряда
    path("create/", OrdersCreateView.as_view(), name="create-order"),

    # Изменение наряда
    path("update/<int:pk>", OrdersUpdateView.as_view(), name="update-order"),

    # Завершение наряда
    path("<int:pk>/confirm-delete", OrderCompleteView.as_view(), name="complete-order"),

    # Список оборудования
    path("eq/", eq_page, name="eq"),

    # Создание оборудования
    path("eq/create/", EqCreateView.as_view(), name="create-eq"),

    # Редактирование оборудования
    path("eq/update/<int:pk>", EqUpdateView.as_view(), name="update-eq"),
]