from django.db import models

# Create your models here.
class Student(models.Model):
 name = models.CharField(max_length=70)
 roll = models.IntegerField(unique=True, null=False)
 city = models.CharField(max_length=70)
 marks = models.IntegerField()
 pass_date = models.DateField()

 def __str__(self):
  return self.name
 

class Teacher(models.Model):
 name = models.CharField(max_length=70)
 empnum = models.IntegerField(unique=True, null=False)
 city = models.CharField(max_length=70)
 salary = models.IntegerField()
 join_date = models.DateField()

 def __str__(self):
  return self.name
 

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
  description = models.TextField(max_length=100)
  published_date = models.DateField()
  published_year = models.IntegerField(null=True,blank=True,default=2002)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  is_activae = models.BooleanField(default=True)

  def __str__(self):
    return self.title
  
class Reviews(models.Model):
  book = models.ForeignKey(Book,on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.CharField(max_length=100)

  def __str__(self):
   return self.book