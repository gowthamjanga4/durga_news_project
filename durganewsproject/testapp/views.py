from django.shortcuts import render


# Create your views here.

# This is first view
def index_view(request):
    return render(request, 'testapp/index.html')

# This is second view
def movies_view(request):
    msg1 = 'pushpa2 released in december and became blockbuster'
    msg2 = 'Mahesh and rajamouli movie workshop begins'
    msg3 = 'sukumar is planning a movie with ramcharan'
    return render(request, 'testapp/movies.html', {'msg1': msg1, 'msg2': msg2, 'msg3': msg3})


def politics_view(request):
    msg1 = 'Modi became pm again in 2024'
    msg2 = 'Waqf bill was shifted to next budget sessions'
    msg3 = 'There is so much violence is happening against hindus in bangladesh'
    return render(request, 'testapp/politics.html', {'msg1': msg1, 'msg2': msg2, 'msg3': msg3})


def sports_view(request):
    msg1 = 'Virat kohli hit century'
    msg2 = 'Jai shah will be the next icc president'
    msg3 = 'BCCI confirmed that not sending the indian cricket players to pakistan'
    return render(request, 'testapp/politics.html', {'msg1': msg1, 'msg2': msg2, 'msg3': msg3})
