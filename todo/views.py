from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Todo, EditForm
from .serializers import TodoSerializer
from django.http import HttpResponse

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Displays all the object in the index page
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos,})

# When called, it creates a new object then displays the updated db table
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        if title != '':
            due_date = request.POST['due_date']

            Todo.objects.create(title = title, due_date = due_date)
            todos = Todo.objects.all()
            return render(request, 'todo/index.html', {'todos': todos,})

# Picks up the object from db using pk, then updates the form using ModalForm
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

# Fetches the object using pk then deletes it.
def delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        todo = get_object_or_404(Todo, pk=int(id))
        print(todo)
        todo.delete()

        todos = Todo.objects.all()
        return render(request, 'todo/index.html', {'todos': todos,})