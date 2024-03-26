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
                size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
                value_activity = float(row['Valor atividade'].replace('.', '').replace(',', '.').replace('R$', ''))
                total_activity = float(row['Total atividade'].replace('.', '').replace(',', '.').replace('R$', ''))

                Activity.objects.create(
                    size=size,
                    name=row['Atividade'],
                    valueActivity=value_activity,
                    totalActivity=total_activity
                )

            return redirect('/activities/get')
    else:
        form = CSVImportForm()
    return render(request, 'import_csv_activities.html', {'form': form})


@login_required
def get(request):
    activity_list = Activity.objects.all()
    return render(
        request,
        'get_activities.html',
        {
            "activityList": activity_list
        }
    )
