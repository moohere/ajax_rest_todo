from django.utils import timezone
from django.db import models
from django.forms import ModelForm

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 250)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return self.title

class EditForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ['created']
        #fields = ['title', 'created', 'due_date']
