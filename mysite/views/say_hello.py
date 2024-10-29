from django.http import HttpResponse, HttpRequest

def say_hello(request):
	return HttpResponse("Hello world!!")

def say_hello_name(request: HttpRequest, name):
	print(request.headers)
	return HttpResponse("Hello %s!!" % name)