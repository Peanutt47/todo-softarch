from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from todo.forms import TodoForm
from django.contrib import messages

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        if 'status' in request.POST:
            todo.status = request.POST['status']
            todo.save()
            return redirect('todo_list')
        else:
            form = TodoForm(request.POST, request.FILES, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form})

@login_required
def delete_todo(request, pk):
    # Fetch the todo object, ensuring it belongs to the logged-in user
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == 'POST':
        # Delete the todo and provide feedback
        todo.delete()
        messages.success(request, f'Todo "{todo.title}" has been deleted successfully.')
        return redirect('todo_list')

    # Render the confirmation page
    return render(request, 'delete_todo.html', {'todo': todo})