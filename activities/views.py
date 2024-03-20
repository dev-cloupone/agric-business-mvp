from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CSVImportForm
from .models import Activity
import csv


@login_required
def import_activities(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                size = row['Hectare'].replace('.', '').replace(',', '.')
                Activity.objects.create(
                    name=row['Talhão'],
                    size=size,
                    activity=activity,
                    valueActivity=valueActivity,
                    totalActivity=totalActivity
                )

            return redirect('/activities/get')
    else:
        form = CSVImportForm()
    return render(request, 'import_csv.html', {'form': form})


@login_required
def get(request):
    activityList = Activity.objects.all()
    print(len(activityList))
    return render(
        request,
        'get_activities.html',
        {
            "activityList": activityList
        }
    )