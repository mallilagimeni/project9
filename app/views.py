from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'sample.html')


def new(request):
    return render(request,'new.html')