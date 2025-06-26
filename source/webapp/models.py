from django.db import models


status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.TextField(verbose_name='Описание', null=False, blank=False)
    status = models.CharField(max_length=50,verbose_name='Статус', null=False, blank=False, choices=status_choices)
    created_at = models.DateField(verbose_name='Дата выполнения', null=True)
    more_detailed = models.TextField(verbose_name='Подробное описание', null=True)


    def __str__(self):
        return f"{self.id} - {self.description}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"

