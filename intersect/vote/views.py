from django.shortcuts import render
from django.http import HttpResponse
from vote.models import Vote, Intersection



# Create your views here.


from django.shortcuts import render

# Create your views here.

def index(request):
    i = Intersection.objects.get(id=1)
    v = Vote(idVote = 1, intersectionIdx= i, response = "mauvaise", description="BAD")
    v.save()

    return HttpResponse("Mauvaise intersection.")
