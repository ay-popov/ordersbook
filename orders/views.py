from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect

from django.urls import reverse, reverse_lazy

from .models import Order, Equipment, Devision
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView
from .forms import OrderCreateForm, EqCreateForm

from django.shortcuts import render


# Завершение наряда
class OrderCompleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("orders:by-date")
    context_object_name = "order"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.status = True
        self.object.save()
        return HttpResponseRedirect(success_url)


# Список нарядов "Мои наряды" для рабочего
def MyOrdersListView(request: HttpRequest):

    context = {
        "orders": (
            Order.objects
            .select_related("devision")
            .prefetch_related("worker")
            .filter(worker__user_id=request.user.id)
            .order_by('order_date').all()
        )
    }

    return render(request=request, template_name="orders/orders_worker.html", context=context)


# Список нарядов на выбранную дату
def OrdersByDateListView(request: HttpRequest):

    orders_date = request.GET.get("date")
    orders_devision = request.GET.get("devision")

    if not orders_date:
        orders_date = str(datetime.now().date())

    if not orders_devision:
        orders_devision = 0
    orders_devision = int(orders_devision)

    cus_date = datetime.strptime(orders_date, "%Y-%m-%d").date()
    parameters = {
        'dev_id': int(orders_devision),
        'ord_date': str(cus_date.strftime("%d.%m.%Y"))
    }

    if orders_devision == 0:
        context = {
            "orders": (
                Order.objects
                .select_related("devision")
                .prefetch_related("worker")
                .filter(order_date=orders_date)
                .order_by('pk').all()
            ),
            "devisions": (
                Devision.objects
                .order_by('pk').all()
            ),
            "params": (
                parameters
            )
        }

    else:
        context = {
            "orders": (
                Order.objects
                .select_related("devision")
                .prefetch_related("worker")
                .filter(order_date=orders_date)
                .filter(devision_id=orders_devision)
                .order_by('pk').all()
            ),
            "devisions": (
                Devision.objects
                .order_by('pk').all()
            ),
            "params": (
                parameters
            )
        }

    return render(request=request, template_name="orders/index.html", context=context)


# Список оборудования
def eq_page(request: HttpRequest):
    context = {
        "equipments": (
            Equipment
            .objects
            .all()
        )
    }
    return render(request=request, template_name="orders/equipment.html", context=context)


# Создание наряда
class OrdersCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def get_success_url(self):
        return reverse("orders:by-date")


# Изменение наряда
class OrdersUpdateView(UpdateView):
    model = Order
    form_class = OrderCreateForm

    def get_success_url(self):
        return reverse("orders:by-date")


# Создание оборудования
class EqCreateView(CreateView):
    model = Equipment
    form_class = EqCreateForm

    def get_success_url(self):
        return reverse("orders:eq")


# Редактирование данных оборудования
class EqUpdateView(UpdateView):

    model = Equipment
    form_class = EqCreateForm

    def get_success_url(self):
        return reverse("orders:eq")


class EquipmentDetailView(DetailView):
    template_name = "equipment.html"
    context_object_name = "Equipment"
    queryset = (Equipment.objects.all())