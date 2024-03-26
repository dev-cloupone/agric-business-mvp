from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Field, Activity, Supplie
import csv

@login_required
def home(request):
    if request.method == 'POST':
        campo = request.POST.get('campo')
        csv_file = request.FILES.get('csv_file')

        if campo == 'fields':
            if csv_file:
                csv_data = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(csv_data)
                for row in csv_reader:
                    size = row['Hectare'].replace('.', '').replace(',', '.')
                    Field.objects.create(
                        name=row['Talhão'],
                        size=size
                    )
                return redirect('/fields/get')

        elif campo == 'activities':
            if csv_file:
                csv_data = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(csv_data)
                for row in csv_reader:
                    size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
                    value_activity = float(
                        row['Valor atividade'].replace('.', '').replace(',', '.').replace('R$', ''))
                    total_activity = float(
                        row['Total atividade'].replace('.', '').replace(',', '.').replace('R$', ''))

                    Activity.objects.create(
                        size=size,
                        name=row['Atividade'],
                        valueActivity=value_activity,
                        totalActivity=total_activity
                    )
                return redirect('/activities/get')

        elif campo == 'supplies':
            if csv_file:
                csv_data = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(csv_data)
                for row in csv_reader:
                    size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
                    size_supplie = float(row['Insumo por hectare'].replace('.', '').replace(',', '.'))
                    value_supplie = float(
                        row['Valor insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
                    total_supplie = float(
                        row['Total insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
                    Supplie.objects.create(
                        name=row['Talhão'],
                        size=size,
                        sizeSupplie=size_supplie,
                        valueSupplie=value_supplie,
                        totalSupplie=total_supplie
                    )
                return redirect('/supplies/get')

    fields = Field.objects.all().order_by('-size').values()[:10]
    nameList_fields = [field['name'] for field in fields]
    sizeList_fields = [str(field['size']) for field in fields]

    activities = Activity.objects.all().order_by('-size').values()[:10]
    nameList_activities = [activity['name'] for activity in activities]
    valueList_activities = [str(activity['totalActivity']) for activity in activities]

    supplies = Supplie.objects.all().order_by('-size').values()[:10]
    nameList_supplies = [supplie['name'] for supplie in supplies]
    valueList_supplies = [str(supplie['totalSupplie']) for supplie in supplies]

    data = {
        "fields": {
            "categories": nameList_fields,
            "series": [
                {"name": "Fields", "data": sizeList_fields}
            ]
        },
        "activities": {
            "categories": nameList_activities,
            "series": [
                {"name": "Activities", "data": valueList_activities}
            ]
        },
        "supplies": {
            "categories": nameList_supplies,
            "series": [
                {"name": "Supplies", "data": valueList_supplies}
            ]
        }
    }
    return render(request, 'home.html', {'chart_data': data})
