from django.db import models

# Create your models here.
departments = (
    ('HR','HR'),
    ('Social Media Handler','Social Media Handler'),
    ('Programmer','Programmer'),
)
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    department = models.CharField(choices=departments,max_length=80)
    salary = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'user'

