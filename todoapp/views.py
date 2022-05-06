from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Todolist
import datetime
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        do_date = request.POST.get('datetime')
        do_date = datetime.datetime.strptime(do_date,
                                                '%d/%m/%Y %H:%M:%S') 
        Todolist.objects.create(title=title,description=description,
                                do_date=do_date)
        messages.success(request, 'New TODO added!')                        
        return redirect(home)

    
    todos = Todolist.objects.filter(deleted=False)
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)


def delete(request, key):
    todo = Todolist.objects.filter(id=key, deleted=False)
    if todo:
        todo.update(deleted=True)
        messages.success(request, 'TODO deleted!') 
    else:
        messages.error(request, 'Invalid TODO!')     

    return redirect(home)    


def edit(request, key):
    todo = Todolist.objects.filter(id=key, deleted=False)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        do_date = request.POST.get('datetime')
        do_date = datetime.datetime.strptime(do_date,
                                                '%d/%m/%Y %H:%M:%S') 
        todo.update(title=title, description=description, 
                    do_date=do_date, status=status)
        messages.success(request, 'Updated!')                        
        return redirect('/edit/'+key)

    else:
        if todo:
            todo = Todolist.objects.get(id=key, deleted=False)
            do_date = todo.do_date
            do_date = do_date.strftime('%d-%m-%Y %H:%M:%S')
            context = {
                'todo': todo,
                'do_date': do_date,
            }
            return render(request, 'edit.html', context)        

        else:
            messages.error(request, 'Invalid TODO!')     

        return redirect(home) 


def get_one(request, key):
    todo = Todolist.objects.filter(id=key, deleted=False)
    if todo:
        todo = Todolist.objects.get(id=key, deleted=False)
        context = {
            'title': todo.title,
            'description': todo.description,
            'status': todo.status,
            'do_date': todo.do_date,
            'created_at': todo.created_at,
            'modified_at': todo.modified_at,
        }
        return JsonResponse(context, safe=False)
    else:
        return JsonResponse("Invalid", safe=False)

def get_all(request):
        todos = Todolist.objects.filter(deleted=False).all()  
        context = {
            'todo': list(todos.values())
        }
        return JsonResponse(context)