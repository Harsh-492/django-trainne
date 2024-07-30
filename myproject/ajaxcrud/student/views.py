from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import User

class HomeView(View):
    def get(self, request):
        fm = StudentRegistrationForm()
        stu = User.objects.all().values()
        return render(request, 'student/home.html', {'form': fm, 'stu': stu})

class SaveDataView(View):
    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            
            if sid == '':
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=sid, name=name, email=email, password=password)
            usr.save()
            
            student_data = list(User.objects.values())
            return JsonResponse({"status": 'Save', 'student_data': student_data})
        else:
            return JsonResponse({"status": 0})

class DeleteDataView(View):
    def post(self, request):
        id = request.POST.get('sid')
        try:
            pi = User.objects.get(pk=id)
            pi.delete()
            return JsonResponse({'status': 1})
        except User.DoesNotExist:
            return JsonResponse({'status': 0})

class EditDataView(View):
    def post(self, request):
        id = request.POST.get('sid')
        try:
            student = User.objects.get(pk=id)
            student_data = {'id': student.id, 'name': student.name, 'email': student.email, 'password': student.password}
            return JsonResponse(student_data)
        except User.DoesNotExist:
            return JsonResponse({'status': 0})
