from django.shortcuts import render
from django.views.generic import View
from .models import Student,Teacher,Book,Author
from django.db.models import Q,Max,Min,Sum,Avg,Count,Subquery,OuterRef,Case,When,CharField,Value
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(View):

    def get(self,request):
        # students = Student.objects.all()
        # students = Student.objects.get(pk=1)
        # students = Student.objects.filter(marks__gt= 90)
        # students = Student.objects.exclude(marks__lt=50)s
        # students = Student.objects.order_by('marks')
        # students = Student.objects.order_by('-marks')
        # students = Student.objects.order_by('id').reverse()[:4]
        # students = Student.objects.values()
        # students = Student.objects.values_list('name','city')
        # students = Student.objects.using('default')


        # and-or operators
        # students = Student.objects.filter(marks__gt=70) & Student.objects.filter city='Surat')
        # students = Student.objects.filter(marks__gt=70,city='Surat') 
        # students = Student.objects.filter(Q(marks__gt=70) & Q(city='Surat') )


        # students = Student.objects.filter(Q(marks__gt=70) | Q(city='Surat'))
        # students = Student.objects.filter(marks__gt=70) | Student.objects.filter(city = 'Rajkot')
        students = Student.objects.all()
        # students = Student.objects.in_bulk([1, 2])
        # print(students.exists())
        queryset = Student.objects.annotate(
                total_comments=Count('marks'),  # Count related objects
                total_likes=Sum('marks'),          # Sum of a field
                avg_rating=Avg('marks')           # Average of a field
        )   
        # print(queryset.total_likes)
        # print('student : ',students)

        
        # ----------------------------Django Look ups---------------------
        # students = Student.objects.filter(name__exact='Harved')
        # students = Student.objects.filter(name__iexact='harved')
        # students = Student.objects.filter(name__contains='a')  
        # students = Student.objects.filter(name__icontains='a')
        # students = Student.objects.filter(id__in = [3,4,6])
        # students = Student.objects.filter(marks__gt = 90)
        # students = Student.objects.filter(marks__gte = 190)
        # students = Student.objects.filter(marks__lt = 190)
        # students = Student.objects.filter(marks__lte = 190)
        # students = Student.objects.filter(name__startswith = 'H')
        # students = Student.objects.filter(name__istartswith = 'H')
        # students = Student.objects.filter(name__endswith = 'd')
        # students = Student.objects.filter(name__iendswith = 'D')
        # students = Student.objects.filter(pass_date__range=('2024-04-01', '2024-12-03'))
        # students = Student.objects.filter(pass_date__year=2024)
        # students = Student.objects.filter(pass_date__month=7)
        # students = Student.objects.filter(pass_date__month__gt=7)
        # students = Student.objects.filter(pass_date__month__gte=7)
        # students = Student.objects.filter(pass_date__day=10)
        # students = Student.objects.filter(pass_date__day__gte=7)
        # students = Student.objects.filter(pass_date__week = 30)
        # students = Student.objects.filter(pass_date__week__gte=30)
        #students = Student.objects.filter(pass_date__quarter = 2)
        #students = Student.objects.filter()
        #  ------------------------------------------------------------------------




        return render(request,'student/studentList.html',{'students':students,'queryset':queryset})  
    
class StudentDetailView(View):

    def get(self,request,pk):
        student = Student.objects.get(pk=pk)
        student_data = Student.objects.all()
        average = student_data.aggregate(Avg('marks'))
        total = student_data.aggregate(Sum('marks'))
        minimum = student_data.aggregate(Min('marks'))
        maximum = student_data.aggregate(Max('marks'))
        totalcount = student_data.aggregate(Count('marks'))
        print((maximum))
        return render(request,'student/studentDetail.html',{'students':student,'average':average['marks__avg'],'total':total['marks__sum'],'minimum':minimum['marks__min'],'maximum':maximum['marks__max']})
    


class GenreralData(View):

    def get(self, request):
        # stu = Student.objects.values_list('name','city',named=True)
        # stu = Student.objects.values('name','city') # it already return value with field name
        # stu = Student.objects.values_list('name','city',named=True) # if named=True then give you value with field value
        s1 = Student.objects.values_list('name','city',named=True)
        s2 = Teacher.objects.values_list('name','city',named=True)
        # stu = s1.union(s2,all=True) #c-10 all-true 
        # stu = s1.intersection(s2) #
        # stu  = s1.difference(s2) #
        # stu = Student.objects.first()
        # stu = Student.objects.last()
        # stu = Student.objects.latest('pass_date')
        # stu = Student.objects.earliest('pass_date')
        # stu = Student.objects.create(name='Harved', roll=70, city='Baroda', marks=90, pass_date='2024-5-7')
        # subquery = Book.objects.filter(author=OuterRef('pk'),published_year__gt=200)
        # author = Author.objects.filter(pk__in=Subquery(subquery.values()))
        # print('subquery : ',subquery)
        # print('author : ',author)
        # count = stu.count()
        # print('count : ',count)
        # student = Student.objects.annotate(marks_cat=Case(When(marks__gt=180,then=Value('Well Done')),When(marks__gt=150,then=Value('Good')),output_field=CharField(),)
        student = Student.objects.annotate(marks_cat=Case(
            When(marks__gt=190,then=Value('Well Done')),
            When(marks__gt=170,then=Value('Good')),
            default=Value('Better Luck Next Time !!!'),
            output_field=CharField()))


        # total_price_after_discount = Student.objects.aggregate(total=Sum(F('price') - F('discount')))['total']
        # Get products where the price is greater than the discount
        # products = Product.objects.filter(price__gt=F('discount'))

        # Update all products by applying their discount
        # Product.objects.update(price=F('price') - F('discount'))


        print('student : ',student.values())
        return render(request,'student/genreral.html',{'students':s1})
    


class StudentCreateViews(View):

    
    def get(self, request):
        
        # stu = Student.objects.create(name='Mayank', roll=30, city='USA', marks=-90, pass_date='3024-5-7')
        # stu = Student.objects.get_or_create(name='Jenil', roll=77, city='Mumbai', marks=50, pass_date='2024-5-7')
        # stu = Student.objects.update_or_create(name='Mayur', roll=30, city='USA', marks=-90, pass_date='3024-5-7')
        
        # objs = [
        #     Student(name='Atif', roll=116, city='Dhanbad', marks=70, pass_date='2020-5-4'),
        #     Student(name='Sahil', roll=117, city='Bokaro', marks=50, pass_date='2020-5-6'),
        #     Student(name='Kumar', roll=118, city='Dhanbad', marks=30, pass_date='2020-5-9'),
        # ]
        # stu = Student.objects.bulk_create(objs)
        # all_student2002_data = Student.objects.all()
        # for stu in all_student_data:
        #     stu.city = 'Dhanbad'
        # stu = Student.objects.bulk_update(all_student_data, ['city'])

        # Annotation fire in terminal
        # Student.objects.values('pass_date').annotate('pass_date')
        # Student.objects.values('name').annotate('city')
        stu = Student.objects.in_bulk([1, 2])
        print(stu)  
        # count = stu.count()
        # print('count : ',count)
        return render(request,'student/studentDetail.html',{'students':stu})
    

class StudentDelete(View):
    success_url = reverse_lazy('list')
    def get(self, request):
        
        # student_data = Student.objects.get(pk=19).delete()
        students = Student.objects.all()
        # student_data = Student.objects.filter(marks=50).delete()
        # student_data = Student.objects.all().delete()
        return render(request,'student/studentList.html',{'students':students}) 
