from django.shortcuts import render, redirect

from django.views import View

from todo.forms import TaskForm, CommentForm, TagForm
from todo.models import Task, Comment, Tag
#from django import forms

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        tasks = Task.objects.all().order_by('-id')
        task_form = TaskForm()

        return render(
            request=request,
            template_name='list.html',
            context={'task_list': tasks, 'task_form': task_form},
        )

    def post(self, request):
        '''POST the data in the form submitted by the user, creating a new task in the todo list'''
        form = TaskForm(request.POST)
        form.save()

        # "redirect" to the todo homepage
        return redirect('todo_list')


class TodoDetailView(View):
    def get(self, request, task_id):
        '''GET the detail view of a single task on the todo list'''
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        comments = Comment.objects.filter(task=task).order_by('created_at')
        comment_form = CommentForm(task=task)
        #print(comments)
        tags = Tag.objects.filter(task=task)
        tag_form = TagForm(task=task)
        print(tags)

        return render(
            request=request,
            template_name='detail.html',
            context={'task_form': task_form, 'id': task_id, 'comments': comments, 'comment_form': comment_form, 'tag_form': tag_form, 'tags':tags},
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.get(id=task_id)

        if 'save_task' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()

        elif 'delete_task' in request.POST:
            task.delete()
 
        elif 'save_comment' in request.POST:
            comment_form = CommentForm(request.POST, task=task)
            comment_form.save()

            return redirect('task', task_id=task.id)

        elif 'add_tag' in request.POST:
            tag_form = TagForm(request.POST, task=task)
            # if tag_form.is_valid():
            tag_form.save()
            

        # "redirect" to the todo homepage
            return redirect('task', task_id=task.id)

        return redirect('todo_list')


