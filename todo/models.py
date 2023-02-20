from django.db import models
from django.urls import reverse
from django.utils import timezone


class TodoList(models.Model):
    tasks = models.CharField(max_length=250, help_text="Задание:")
    status = models.BooleanField(default=False, help_text="Статус выполнения:")
    date_and_time_of_creation = models.DateTimeField(
        default=timezone.now(), help_text="Задание создано:"
    )
    estimated_and_time_of_completion = models.DateTimeField(
        default=timezone.now(), help_text="Задание назначено на:"
    )
    date_and_time_of_completion = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        help_text="Задание переведено в статус 'Выполнено':",
    )

    def get_absolute_url(self):
        return reverse("todolist", args=[self.id])

    def save(self, *args, **kwargs) -> None:
        if self.status is False:
            self.date_and_time_of_completion = None
        else:
            if self.date_and_time_of_completion is None:
                self.date_and_time_of_completion = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"TodoList {self.id}|{self.tasks}|{self.status}|{self.date_and_time_of_creation}|{self.date_and_time_of_completion}"
