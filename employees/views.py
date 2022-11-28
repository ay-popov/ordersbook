from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .models import Employee
from .forms import EmployeeCreateForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


class EmployeesListView(ListView):

    template_name = "employees/index.html"
    context_object_name = "employees"

    queryset = (
        Employee.objects
        .select_related("job")
        .order_by('surname').all()
        )


class EmployeeDetailView(DetailView):
    template_name = "employees/details.html"
    context_object_name = "employee"
    queryset = (Employee.objects.select_related("job"))


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy("employees:index")
    context_object_name = "employee"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class EmployeeCreateView(CreateView):

    model = Employee
    form_class = EmployeeCreateForm

    def get_success_url(self):
        return reverse("employees:details", kwargs={"pk": self.object.pk})


class EmployeeUpdateView(UpdateView):

    model = Employee
    form_class = EmployeeCreateForm

    def get_success_url(self):
        return reverse("employees:index")
