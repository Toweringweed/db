from django.shortcuts import render

# Create your views here.
def repair(request):
    return render(request, 'repair.html')
