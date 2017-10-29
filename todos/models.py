from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def is_unfinished(self):
        return self.done

    is_unfinished.admin_order_field ='unfinished'
    is_unfinished.boolean = True
    is_unfinished.shor_description = "Task not finish yet"
