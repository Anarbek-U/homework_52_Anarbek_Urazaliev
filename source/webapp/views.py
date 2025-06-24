from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task


def index(request):
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get('description')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')
        Task.objects.create(description=description, status=status, created_at=created_at)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'create_task.html')


