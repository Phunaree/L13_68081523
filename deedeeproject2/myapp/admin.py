from django.contrib import admin
from .models import Person

# ลงทะเบียน Model Person ให้โผล่ในหน้า Admin
admin.site.register(Person)