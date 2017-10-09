from django.shortcuts import render

# Create your views here.

def rolepoint_view(request):
	context = {}
	return render(request, 'rolepoint.html', context)


def dashboard_view(request):
	context = {}
	return render(request, 'dashboard.html', context)
