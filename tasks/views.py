from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework import generics
from employees.models import Employee
from .models import Task
from .serializers import TaskSerializer


class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks/list.html', {'tasks': tasks})


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'tasks/create.html', {'employees': employees})

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            employee_id=request.POST['employee'],
        )
        return redirect('tasks:list')


class TaskUpdateStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        new_status = request.POST['status']
        if new_status in dict(Task.Status.choices):
            task.status = new_status
            task.save()
        return redirect('tasks:list')


class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks:list')


class TaskListAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
