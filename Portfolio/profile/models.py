from django.db import models

# Create your models here.


class Company(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/company')


class Position(models.Model):
    # This could be many-to-many, but I think it is more common
    # that employee has different tasks in several companies on same position
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    in_position_from = models.DateField()
    in_position_to = models.DateField(null=True, blank=True)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Technology(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/technology')
    tasks = models.ManyToManyField(Task)
