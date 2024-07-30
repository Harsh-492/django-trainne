from django.db import models

# Create your models here.

tech = (
    ('Pythons', 'Pythons'),
    ('Javascript', 'Javascript'),
    ('React', 'React'),
    ('Android', 'Android'),
    ('Flutter', 'Flutter'),
    ('Java', 'Java'),
)
class MyProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    technology = models.CharField(choices=tech,max_length=400)
    estimate_hours = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'myproject'


class ProjectModule(models.Model):
    project = models.ForeignKey(MyProject,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name