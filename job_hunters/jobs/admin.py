from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "job")
admin.site.register(models.References)
admin.site.register(models.Experiences)
admin.site.register(models.JobType)
admin.site.register(models.Category)
@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", 'category', 'company', 'job_type')