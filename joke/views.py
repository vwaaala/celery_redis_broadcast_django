from django.shortcuts import render


def index(request):
    context = {
        'joke': 'joke'
    }
    return render(request, 'index.html', context)
