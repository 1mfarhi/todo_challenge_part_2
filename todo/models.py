from django.db import models
#from numpy import true_divide


# Create your models here.

class Tag(models.Model):
    # unique=True will stop multiple tags from being created with the same name
    tag_id = models.AutoField(primary_key=True)
    #new_field = models.CharField(max_length=140, default='Some String')
    name = models.CharField(max_length=30, unique=True)
    #task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=true, null=True)


class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)



class Comment(models.Model):
    body = models.TextField()
    # foreign key from comments table,
    # on_delete deletes comments associated with deleted task
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    