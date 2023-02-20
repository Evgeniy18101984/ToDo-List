from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from todo.models import TodoList


def start(request):
    return render(request, "start.html")


class TodoListView(ListView):
    context_object_name = "todolist_"
    model = TodoList
    template_name = "todolist_list.html"


class TodoListViewActive(ListView):
    context_object_name = "todolist_"
    queryset = TodoList.objects.filter(status=False)
    template_name = "todolist_list_not_active.html"


class TodoDetailView(DetailView):
    context_object_name = "todolist"
    model = TodoList
    template_name = "todolist_detail.html"


class TodoCreateView(CreateView):
    model = TodoList
    fields = ["tasks", "status", "estimated_and_time_of_completion"]
    template_name = "todolist_create.html"
    success_url = "/todolist/"


class TodoUpdateView(UpdateView):
    model = TodoList
    fields = ["tasks", "status", "estimated_and_time_of_completion"]
    template_name = "todolist_update.html"
    success_url = "/todolist/"


class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = "todolist_delete.html"
    success_url = "/todolist/"
