from django.contrib import admin
from .models import TaskApp
# Register your models here.

@admin.register(TaskApp)
class TaskAppAdmin(admin.ModelAdmin):
    list_display = ['taskName','description','completedTill',]