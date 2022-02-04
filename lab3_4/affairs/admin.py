from django.contrib import admin
from .models import user,Intake,Trainee,Track
# Register your models here.
admin.site.register(user)
admin.site.register(Intake)
admin.site.register(Track)