from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Application)
admin.site.register(models.References)
admin.site.register(models.Experiences)
admin.site.register(models.JobType)
admin.site.register(models.Category)
admin.site.register(models.Job)
