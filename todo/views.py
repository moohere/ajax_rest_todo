from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Todo, EditForm
from .serializers import TodoSerializer
from django.http import HttpResponse

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos,})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        due_date = request.POST['due_date']

        Todo.objects.create(title = title, due_date = due_date)
        todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'todos': todos,})

def edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        due_date = str(request.POST['due_date'])
        id = request.POST['id']

        todo = get_object_or_404(Todo, pk=int(id))
        
        form = EditForm({'title':title, 'due_date':due_date}, instance = todo)
        form.save() 

        todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'todos': todos,})

def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        todo = get_object_or_404(Todo, pk=int(id))
        todo.delete()

        todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'todos': todos,})