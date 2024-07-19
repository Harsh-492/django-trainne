from django.contrib import admin
from .models import MyProject
# Register your models here.

@admin.register(MyProject)
class AdminProject(admin.ModelAdmin):
    list_display = ['id','title','description','technology','start_date','end_date','estimate_hours']