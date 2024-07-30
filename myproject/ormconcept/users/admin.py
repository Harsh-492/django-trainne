from django.contrib import admin
from .models import Student,Teacher,Book,Reviews,Author
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll','city','marks','pass_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'empnum','city','salary','join_date']


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','birth_date']   

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','description','price','published_year']

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','book','rating']
