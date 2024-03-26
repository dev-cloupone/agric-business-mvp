from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CSVImportForm
from .models import Supplie
import csv


@login_required
def import_supplies(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                size = float(row['Tamanho'].replace('.', '').replace(',', '.'))
                size_supplie = float(row['Insumo por hectare'].replace('.', '').replace(',', '.'))
                value_supplie = float(row['Valor insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
                total_supplie = float(row['Total insumo'].replace('.', '').replace(',', '.').replace('R$', ''))
                Supplie.objects.create(
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
    supplie_list = Supplie.objects.all()
    return render(
        request,
        'get_supplies.html',
        {
            "supplieList": supplie_list
        }
    )