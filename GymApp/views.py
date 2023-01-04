from django.shortcuts import render, redirect
from . models import TestModel
from . forms import TestForm
from django.http import HttpResponse
import csv

# Create your views here.
def Search(request):
    if request.method == "POST":
        Searching = request.POST['Searching']
        Results_query = TestModel.objects.filter(Name__contains=Searching)
        {'Searching':Searching,
        'Results_query':Results_query}
    return render(request, 'GymApp/Searching.html',
    {'Searching':Searching,
        'Results_query':Results_query})

def DownloadingCSV(request):
        response = HttpResponse(content_type='text/csv')
        response['content-disposition'] = 'attachment; filename=Client_list.csv'

        writer = csv.writer(response)
        Downloading_all = TestModel.objects.all()
        writer.writerow(['Name','Surname',
                        'Weight','Height',
                        'Outcome','Gender',
                        'Activity'])
        for download in Downloading_all:
            writer.writerow([download.Name,
                        download.Surname,
                        download.Weight,
                        download.Height,
                        download.Outcome,
                        download.Gender,
                        download.Activity])
        return response 

def Client_Delete(request, Client_id):
    ClientUpdate = TestModel.objects.get(pk=Client_id)
    ClientUpdate.delete()
    return redirect('Home')

def Client_Update(request, Client_id):
    ClientUpdate = TestModel.objects.get(pk=Client_id)
    ClientUpdates = TestForm(request.POST or None, instance=ClientUpdate)
    if request.method == 'POST':
       if ClientUpdates.is_valid():
        ClientUpdates.save()
        return redirect('Client_list')
    return render(request, 'GymApp/ClientUpdate.html',
    {'ClientUpdate':ClientUpdate,
    'ClientUpdates':ClientUpdates})

def Client_list(request):
    Clients = TestModel.objects.all()
    return render(request, 'GymApp/ClientList.html',
    {'Clients':Clients})

def Client_Details(request, Client_id):
    ClientDetails = TestModel.objects.get(pk=Client_id)
    return render(request, 'GymApp/ClientDetails.html',
    {'ClientDetails':ClientDetails})

def Home(request):
    Forms = TestForm
    if request.method == 'POST':
        Forms = TestForm(request.POST or None)
        if Forms.is_valid():
            Forms.save()
            return redirect('Client_list')
    return render(request, 'GymApp/Home.html',{})
