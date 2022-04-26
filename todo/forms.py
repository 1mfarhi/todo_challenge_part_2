from xml.etree.ElementTree import Comment
from django import forms

from todo.models import Task, Comment
# class TaskForm(forms.Form):
#     description = forms.CharField(label='Add task', max_length=255)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['description'].label = 'Add Task'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']        
    
    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task')
        super().__init__(*args, **kwargs)
        self.instance.task = task
        self.fields['comment'].label = 'Add A Comment'


