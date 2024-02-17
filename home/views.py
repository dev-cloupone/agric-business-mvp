from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fields.models import Field

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
