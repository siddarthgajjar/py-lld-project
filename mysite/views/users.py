from django.http import HttpResponse, HttpRequest
from ..models import User
import json
from django.shortcuts import get_object_or_404

def users(request: HttpRequest) -> HttpResponse:
	if request.method == "GET":
		users = User.objects.all()
		serialized_users = [user.name for user in users]
		return HttpResponse(json.dumps(serialized_users))

	if request.method == "POST":
		body = json.loads(request.body)
		user = User(username=body['username'], name=body['name'], email=body['name'])
		user.save()
		return HttpResponse(json.dumps({"id": user.id, "name": user.name}))

def update_delete_user(request: HttpRequest, id: int) -> HttpResponse:


	if request.method == "GET":
		user = get_object_or_404(User, id=id)
		return HttpResponse(json.dumps({"id": user.id, "name": user.name}))

	if request.method == "PUT":
		body = json.loads(request.body)
		user = get_object_or_404(User, id=id)
		user.username = body['username']
		user.name = body['name']
		user.email = body['email']
		user.save()
		return HttpResponse(json.dumps({"id": user.id, "name": user.name}))

	if request.method == "DELETE":
		body = json.loads(request.body)
		user = get_object_or_404(User, id=id)
		user.delete()
		return HttpResponse(json.dumps({"id": user.id, "deleted": True}))

