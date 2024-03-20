from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fields.models import Field
from activities.models import Activity

@login_required
def home(request):
    fields = Field.objects.all().order_by('-size').values()[:10]
    nameList = [field['name'] for field in fields]
    sizeList = [str(field['size']) for field in fields]
    data = {
        "categories": nameList,
        "series": [
            {"name": "Fields", "data": sizeList}
        ]
    }
    return render(request, 'home.html', {'chart_data': data})

@login_required
def home(request):
    activities = Activity.objects.all().order_by('-size').values()[:10]
    nameList = [activity['name'] for activity in activities]
    sizeList = [str(activity['size']) for activity in activities]
    valueActivityList = Activity.objects.all().order_by('-valueActivity').values()[:10]
    totalActivityList = Activity.objects.all().order_by('-totalActivity').values()[:10]
    data = {
        "categories": nameList,
        "series": [
            {"name": "Fields", "data": sizeList}
        ]
    }
    return render(request, 'home.html', {'chart_data': data})