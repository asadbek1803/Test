from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(LoginRequiredMixin, View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employees/list.html', {'employees': employees})


class EmployeeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'employees/create.html')

    def post(self, request):
        Employee.objects.create(
            full_name=request.POST['full_name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            position=request.POST['position'],
            salary=request.POST['salary'],
            hire_date=request.POST['hire_date'],
        )
        return redirect('employees:list')


class EmployeeEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employees/edit.html', {'employee': employee})

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.full_name = request.POST['full_name']
        employee.phone = request.POST['phone']
        employee.email = request.POST['email']
        employee.position = request.POST['position']
        employee.salary = request.POST['salary']
        employee.hire_date = request.POST['hire_date']
        employee.save()
        return redirect('employees:list')


class EmployeeDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('employees:list')


class EmployeeListAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
