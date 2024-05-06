from django.db import models

# Create your models here.
class JobType(models.Model):
    job_type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.job_type

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=200)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    due_date = models.DateField("Due date")
    start_date = models.DateField("Start date")

class Application(models.Model):
    pass