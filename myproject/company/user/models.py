from django.db import models

# Create your models here.

depart = (
    ('Python Developer', 'Python Developer'),
    ('Java Developer', 'Java Developer'),
    ('MERN', 'MERN'),
    ('Android Developer', 'Android Developer'),
)
class MyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    salary = models.CharField(max_length=8)
    department = models.CharField(max_length=20,choices=depart)

    class Meta:
        db_table = 'myuser'
    
    def __str__(self):
        return self.name
    
    