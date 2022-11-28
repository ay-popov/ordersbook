import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Участок выполнения наряда
class Devision(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name


# Модель оборудования
class Equipment(MPTTModel):
    class Meta:
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=64, verbose_name="Наименование")
    techcode = models.CharField(max_length=64, null=True, verbose_name="Технологический код")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE,
                            verbose_name="Родительская категория")

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        if self.techcode is not None:
            return str(self.name) + '   (' + str(self.techcode) + ")"
        else:
            return str(self.name)

    def get_full_name(self):
        if self.techcode is not None:
            return str(self.name) + '  ' + str(self.techcode)
        else:
            return str(self.name)

    def get_parents(self):
        parents = self.get_full_name()
        for parent in self.get_ancestors(ascending=True, include_self=False):
            parents = parent.name + ' / ' + parents
        return parents


mptt.register(Equipment, order_insertion_by=['name'])


# Модель наряда
class Order(models.Model):
    name = models.CharField(max_length=64, null=False, verbose_name="Наименование работы")
    worker = models.ManyToManyField("employees.employee", related_name="orders", verbose_name="Рабочие")
    order_date = models.DateField(verbose_name="Дата наряда")
    devision = models.ForeignKey(Devision, on_delete=models.PROTECT, related_name="order", default=0,
                                 verbose_name="Участок")
    status = models.BooleanField(default=False)
    equipment = models.ForeignKey(Equipment, related_name="order", on_delete=models.PROTECT, default=0,
                                  verbose_name="Оборудование")
