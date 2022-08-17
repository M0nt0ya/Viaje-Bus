from django.shortcuts import render, redirect
from .models import Task

def list_tasks(request):
    task = Task.objects.all()
    context = {
        "task": task[::-1],
        "update_from": None
    }
    return render(request, 'list_tasks.html', context)


def create_task(request):
    tasks_numeroplaca = request.POST["numeroplaca"]
    tasks_horapartida = request.POST["horapartida"]
    tasks_llegadahora = request.POST["llegadahora"]
    tasks_horaviaje = request.POST["horaviaje"]
    tasks_partida = request.POST["partida"]
    tasks_destino = request.POST["destino"]
    tasks_costo = request.POST["costo"]
    if tasks_numeroplaca== "" or tasks_horapartida== "" or tasks_llegadahora== ""  or tasks_horaviaje== "" or tasks_partida== "" or tasks_destino== "" or tasks_costo== "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "Title and description is required"}
        )
    task = Task(numeroplaca=tasks_numeroplaca, horapartida=tasks_horapartida, llegadahora=tasks_llegadahora, horaviaje=tasks_horaviaje, partida=tasks_partida, destino=tasks_destino, costo=tasks_costo)
    task.save()
    return redirect("/tasks/")


def update(request):
    task_id = request.POST["id"]
    task_numeroplaca = request.POST['numeroplaca']
    task_horapartida = request.POST['horapartida']
    task_llegadahora = request.POST['llegadahora']
    task_horaviaje = request.POST['horaviaje']
    task_partida = request.POST['partida']  
    task_destino = request.POST['destino']  
    task_costo = request.POST['costo']  
    task = Task.objects.get(pk=task_id)
    task.numeroplaca = task_numeroplaca 
    task.horapartida = task_horapartida
    task.llegadahora = task_llegadahora
    task.horaviaje = task_horaviaje
    task.partida = task_partida
    task.destino = task_destino
    task.costo = task_costo
    task.save()
    return redirect("/tasks/")

def update_from(request, task_id):
    task = Task.objects.all()
    task_only = Task.objects.get(pk=task_id)
    print(task_only)
    context = {
        "task": task[::-1],
        "update": task_only
    }
    return render(request, 'list_tasks.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/tasks/")
