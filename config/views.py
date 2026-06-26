from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from employees.models import Employee
from tasks.models import Task
from django.db.models import Count


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        total_employees = Employee.objects.count()
        total_tasks = Task.objects.count()
        task_status_counts = Task.objects.values('status').annotate(count=Count('id'))
        statuses = {item['status']: item['count'] for item in task_status_counts}
        recent_tasks = Task.objects.select_related('employee').order_by('-created_at')[:5]
        recent_employees = Employee.objects.order_by('-id')[:5]

        context = {
            'total_employees': total_employees,
            'total_tasks': total_tasks,
            'tasks_created': statuses.get('created', 0),
            'tasks_in_progress': statuses.get('in_progress', 0),
            'tasks_completed': statuses.get('completed', 0),
            'recent_tasks': recent_tasks,
            'recent_employees': recent_employees,
        }
        return render(request, 'dashboard.html', context)
