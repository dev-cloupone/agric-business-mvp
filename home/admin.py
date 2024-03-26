from django.contrib import admin
from .models import Field
from .models import Activity
from .models import Supplie

admin.site.register(Activity)
admin.site.register(Field)
admin.site.register(Supplie)

# Register your models here.
