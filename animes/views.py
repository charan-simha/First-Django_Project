from django.http import HttpResponse
from django.shortcuts import render

data={
    'animes':[
        {
          'id':5,
          'title':'Naruto',
          'year':2003
        },
        {
          'id':6,
          'title':'OnePiece',
          'year':1998
        },
        {
          'id':7,
          'title':'DBZ',
          'year':2000
        }
    ]
}


def animes(request):
    return render(request, 'animes/animes.html',data)
def home(request):
    return HttpResponse("Home Page")