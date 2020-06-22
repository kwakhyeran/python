from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return f'{self.name} : {self.age}'
class Album(models.Model):
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    def __str__(self):
        return f'{self.title} / {self.release_date}'

