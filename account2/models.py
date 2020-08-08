from django.db import models
from django.conf import settings
# Create your models here.
class   Profile2(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date_of_birth=models.DateField(null=True)
	photo=models.ImageField(upload_to='media/%y/%d/%m')

	def __str__(self):
		return 'Profile name {}'.format(self.user.username)
		