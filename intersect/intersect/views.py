from django.template import loader
from django.shortcuts import render
from vote.models import Intersection, Intervention, Action
from math import radians, sin, cos, acos
from itertools import chain
from django.db.models.query import EmptyQuerySet




def home(request):

	#intersectionList = Intersection.objects.all()[:5]
	#intersectionList = Intersection.objects.get(id=1)


	#Quebec
	pos_lat = 46.802335
	pos_lon = -71.229034


	#Quebec2

	#pos_lat = 46.81023
	#pos_lon = -71.239179

	#Quebec3

	#pos_lat = 46.770342
	#pos_lon = -71.278447

	pos_lat = radians(pos_lat)
	pos_lon = radians(pos_lon)




	ongoing_interventions = Intervention.objects.filter(status = 'En cours')


	#intersectionList= Intersection.objects.none()


	intersectionList = list()
	secondList = list()
	minDistance=100;



	for intervention in ongoing_interventions:

		int_lat = radians(float(Intersection.objects.get(id=intervention.id).latitude))
		int_lon = radians(float(Intersection.objects.get(id=intervention.id).longitude))
		euclideanDistance = 6371.01 * acos(sin(pos_lat)*sin(int_lat) + cos(pos_lat)*cos(int_lat)*cos(pos_lon-int_lon))
		print(euclideanDistance)


		if euclideanDistance < 20 :
			intersection = Intersection.objects.filter(id=intervention.id).first()
			intersectionList.append(intersection)

			if(euclideanDistance < minDistance):
				minDistance = euclideanDistance
				intersectionPlusProche = intersection
				action = Action.objects.filter(id=intervention.id)


			intersection = Intersection.objects.filter(id=intervention.id).first()
			intersectionList.append(intersection)



	return render(request, "index.html", {'intersectionList': intersectionList, 'intersectionPlusProche': intersectionPlusProche,
										  'action': action})
	#return render(request, "index.html")



