from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # foreign key from comments table,
    # on_delete deletes comments associated with deleted task
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    

    