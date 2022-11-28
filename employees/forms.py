from django.forms import ModelForm, CharField
from django.forms.widgets import Widget
from .models import Employee


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = "surname", "firstname", "patronymic", "personnel_number", "email", "job", "user", "group", "archived"

    surname = CharField(max_length=40, label="Фамилия")
    firstname = CharField(max_length=40, label="Имя")
    patronymic = CharField(max_length=40, label="Отчество")
    personnel_number = CharField(max_length=8, label="Табельный номер")
    email = CharField(max_length=40, label="Email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget

            if str(field.__class__).find("BooleanField") > 0:
                widget.attrs["class"] = "checkbox"
            else:
                widget.attrs["class"] = "form-control"
