from django.http import HttpResponse

def home (request):
	return HttpResponse("dream league Version 1.00")
