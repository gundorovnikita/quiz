from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
	task = Task.objects.all()
	context={
		'task':task,
	}
	return render(request, 'index.html', context)