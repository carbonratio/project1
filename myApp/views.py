from django.shortcuts import render

# Create your views here.
def index(request):
    mydict = {'injection1': 'Hello World'}
    return render(request, 'myApp/index.html',context=mydict)