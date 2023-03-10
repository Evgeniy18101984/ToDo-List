# Generated by Django 4.1.7 on 2023-02-19 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todolist",
            name="estimated_and_time_of_completion",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 19, 20, 1, 2, 751599),
                help_text="Задание назначено на:",
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="date_and_time_of_completion",
            field=models.DateTimeField(
                blank=True,
                default=None,
                help_text="Задание переведено в статус 'Выполнено':",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="date_and_time_of_creation",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 19, 20, 1, 2, 751599),
                help_text="Задание создано:",
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="status",
            field=models.BooleanField(default=False, help_text="Статус выполнения:"),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="tasks",
            field=models.CharField(help_text="Задание:", max_length=250),
        ),
    ]
