from django.db import models
from rest_framework import serializers

class Orders(models.Model):
    table = models.CharField(max_length=25)
    worker = models.ForeignKey('Workers', on_delete=models.CASCADE, related_name='Workers')
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey("StatusOfOrder", on_delete=models.CASCADE, related_name='Status')
    price = models.IntegerField(null=True, default=10)

    class Meta:
        verbose_name = 'Заказы'

    def __str__(self):
        return str(self.table)

class Workers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    photo = models.URLField(default=None)
    jobtitle = models.ForeignKey("WorkerJobTitle", on_delete=models.PROTECT, related_name='job')

    class Meta:
        verbose_name = 'Работник'

    def __str__(self):
        return str(self.surname)

class WorkerJobTitle(models.Model):
    jobname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Должность'

    def __str__(self):
        return str(self.jobname)

class StatusOfOrder(models.Model):
    ordstatus = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Статус'

    def __str__(self):
        return str(self.ordstatus)

