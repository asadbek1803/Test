from django.db import models


class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    position = models.CharField('Должность', max_length=255)
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2)
    hire_date = models.DateField('Дата приема')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-id']

    def __str__(self):
        return self.full_name
