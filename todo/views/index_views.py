from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo

# Create your views here.
class Index(View):
    def get(self, request):
        """
        Handle GET requests.
        """
        todos = Todo.objects.all()
        return render(request, 'todo_list.html', {'todos': todos})