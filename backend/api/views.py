import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest, JsonResponse
from api.models import Todo, Logs


@csrf_exempt
def create_todo(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return HttpResponse('bad request', status=405)
    data = json.loads(request.body)
    todo = Todo.objects.create(title=data['title'])
    return JsonResponse({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    })


@csrf_exempt
def update_todo(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return HttpResponse('bad request', status=405)
    data = json.loads(request.body)
    todo = Todo.objects.get(id=data["id"])
    todo.completed = data['completed']
    todo.save()
    return JsonResponse({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    })


@csrf_exempt
def delete_todo(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return HttpResponse('bad request', status=405)
    data = json.loads(request.body)
    todo = Todo.objects.get(id=data["id"])
    todo.delete()

    return JsonResponse({
        "id": data['id'],
        "title": todo.title,
        "completed": todo.completed,
    })


@csrf_exempt
def get_todos(request: HttpRequest) -> JsonResponse:
    if request.method != 'GET':
        return HttpResponse('bad reqest', status=405)

    all_todos = [{
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    } for todo in Todo.objects.all()]

    return JsonResponse({"todos": all_todos})


@csrf_exempt
def create_log(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return HttpResponse('bad request', status=405)
    data = json.loads(request.body)
    Logs.objects.create(title=data['action'])
    return JsonResponse({"success": True})


@csrf_exempt
def get_logs(request: HttpRequest) -> JsonResponse:
    if request.method != 'GET':
        return HttpResponse('bad reqest', status=405)
    data = Logs.objects.all()
    return JsonResponse({'logs': data})
