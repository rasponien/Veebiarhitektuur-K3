from django.shortcuts import render
from django.http import JsonResponse
from .models import AnimalObservation, Animal
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def searchByName(request):
    animals = Animal.objects.get_queryset()
    searchKeyWord = request.POST['searchParameter']
    result = []

    for animal in animals:
        if animal.name == searchKeyWord:
            result.append({
                'name' : animal.name,
                'species' : animal.species,
                'observationInfo' : findObservationInfo(animal.id)
            })
    return JsonResponse(result, safe=False)

@csrf_exempt
def searchBySpecies(request):
    animals = Animal.objects.get_queryset()
    searchKeyWord = request.POST['searchParameter']
    result = []

    for animal in animals:
        if animal.species == searchKeyWord:
            result.append({
                'name' : animal.name,
                'species' : animal.species,
                'observationInfo' : findObservationInfo(animal.id)
            })
    return JsonResponse(result, safe=False)

@csrf_exempt
def removeAnimal(request):

    animals = Animal.objects.get_queryset()
    searchKeyWord = request.POST['animalName']

    animalToDelete = Animal.objects.filter(name = searchKeyWord)
    animalToDelete.delete();

    result = []

    for animal in animals:
        if animal.species == searchKeyWord:
            result.append({
                'name' : animal.name,
                'species' : animal.species,
                'observationInfo' : findObservationInfo(animal.id)
            })
    return JsonResponse(result, safe=False)






def findObservationInfo(id):
    observationData = []
    for record in AnimalObservation.objects.filter(animal_id = id):
        observationData.append({
            'location' : record.last_seen_location,
            'datetime' : str(record.last_seen_time)
        })
    return observationData

