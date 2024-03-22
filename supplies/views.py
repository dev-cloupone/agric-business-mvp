from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CSVImportForm
from .models import supplie
import csv


@login_required
def import_supplies(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                size = row['Tamanho'].replace('.', '').replace(',', '.')
                size_supplie = row['Insumo por hectare'].replace('.', '').replace(',', '.')
                value_supplie = row['Valor insumo'].replace('.', '').replace(',', '.')
                total_supplie = row['Total insumo'].replace('.', '').replace(',', '.')
                size = row['Tamanho']
                Activity.objects.create(
                    name=row['Talhão'],
                    size=size,
                    sizeSupplie=size_supplie,
                    valueSupplie=value_supplie,
                    totalSupplie=total_supplie
                )
            return redirect('/supplies/get')
    else:
        form = CSVImportForm()
    return render(request, 'import_csv_supplies.html', {'form': form})


@login_required
def get(request):
    supplie_list = supplie.objects.all()
    return render(
        request,
        'get_supplies.html',
        {
            "supplieList": supplie_list
        }
    )