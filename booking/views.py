from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):


    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html', {
        'data': "hello world"
    }
                  )
