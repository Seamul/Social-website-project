from django.contrib import admin
from .models import Profile2
# Register your models here.
@admin.register(Profile2)
class  Profile2Admin(admin.ModelAdmin):
	"""docstring for  Profile2Model"""
	lidt_desplay=['user','date_of_birth','photo']
