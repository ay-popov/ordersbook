from django.contrib.auth.models import User, Group
from django.db import models


# Должность сотрудника
class JobTitles(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# Модель сотрудника
class Employee(models.Model):
    surname = models.CharField(max_length=64, null=False)
    firstname = models.CharField(max_length=64, null=False)
    patronymic = models.CharField(max_length=64, null=False)
    personnel_number = models.CharField(max_length=64, unique=True, null=False)
    email = models.CharField(max_length=64, null=False)
    job = models.ForeignKey(JobTitles, on_delete=models.PROTECT, related_name="employee", verbose_name="Должность")
    archived = models.BooleanField(default=False, verbose_name='Архив')
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="user", null=True, verbose_name="Пользователь")
    group = models.ForeignKey(Group, on_delete=models.PROTECT, related_name="group", verbose_name="Группа доступа", default=2)

    def __str__(self):
        return f"{self.surname} {self.firstname} ({self.job})"



