from django.db import models
from employees.models import Employee


class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created', 'Создана'
        IN_PROGRESS = 'in_progress', 'В работе'
        COMPLETED = 'completed', 'Выполнена'

    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    status = models.CharField(
        'Статус', max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        verbose_name='Сотрудник', related_name='tasks',
    )
    created_at = models.DateTimeField('Создана', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
