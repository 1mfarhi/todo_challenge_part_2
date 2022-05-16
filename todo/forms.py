from tkinter import NONE
from venv import create
from xml.etree.ElementTree import Comment
from django import forms

from todo.models import Task, Comment, Tag
# class TaskForm(forms.Form):
#     description = forms.CharField(label='Add task', max_length=255)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].label = 'Add Task'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', NONE)
        super().__init__(*args, **kwargs)

        self.instance.task = self.task 
        self.fields['name'].label = '' 

    def save(self, *args, **kwargs):
        # usually, calling <form>.save() will try to create a new instance of the model.
        # In this case, a tag with the given name might already exist. Use get_or_create()
        # to only create one if it does not already exit
        tag, create = Tag.objects.get_or_create(name = self.data['name'])

        # Automatically add this tag to the task, whether it is now or not.
        self.task.tags.add(tag)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    
    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task')
        super().__init__(*args, **kwargs)
        self.instance.task = task
        self.fields['body'].label = ''

