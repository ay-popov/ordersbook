from django.urls import path
from .views import (OrdersCreateView, eq_page, OrdersByDateListView, MyOrdersListView, OrderCompleteView,
                    EqCreateView, OrdersUpdateView)

app_name = "orders"

urlpatterns = [

    path("", OrdersByDateListView, name="by-date"),

    path("my_orders/", MyOrdersListView, name="my_orders"),

    path("create/", OrdersCreateView.as_view(), name="create-order"),

    path("update/<int:pk>", OrdersUpdateView.as_view(), name="update-order"),

    path("<int:pk>/confirm-delete", OrderCompleteView.as_view(), name="complete-order"),

    path("eq/", eq_page, name="eq"),
    path("eq/create/", EqCreateView.as_view(), name="create-eq"),

]