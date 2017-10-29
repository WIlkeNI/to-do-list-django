from django.contrib import admin

from todos.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'done')
    list_filter = ['done']
admin.site.register(Task, TaskAdmin)
