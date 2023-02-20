from django.contrib import admin
from todo.models import TodoList

admin.site.site_url = "http://127.0.0.1:8000/"


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "tasks",
        "date_and_time_of_creation",
        "estimated_and_time_of_completion",
        "date_and_time_of_completion",
        "status",
    ]
    list_filter = ["status"]
    readonly_fields = ["date_and_time_of_creation", "date_and_time_of_completion"]
    search_fields = ("id", "tasks")
    ordering = ["estimated_and_time_of_completion"]
