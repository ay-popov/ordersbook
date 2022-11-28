from django.forms import ModelForm
from django.forms.widgets import Widget
from mptt.forms import TreeNodeChoiceField
from .models import Order, Equipment
from employees import models
from django import forms
from tempus_dominus.widgets import DatePicker


class OrderCreateForm(ModelForm):

    class Meta:
        model = Order
        fields = "name", "worker", "devision", "order_date", "equipment"

    order_date = forms.DateField(
        required=True,
        widget=DatePicker(
        ),
        label="Дата наряда"
    )

    equipment = TreeNodeChoiceField(queryset=Equipment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"

        self.fields['worker'].queryset = models.Employee.objects.filter(group_id=2).filter(archived=0).order_by('surname')
        self.fields['equipment'].label = "Оборудование:"


class EqCreateForm(ModelForm):

    class Meta:
        model = Equipment
        fields = "name", "parent", "techcode"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"

