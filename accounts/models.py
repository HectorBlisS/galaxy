from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth = models.DateField(blank=True, null=True)
	tel = models.IntegerField(default=0, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	cover = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

	def __str__(self):
		return 'Perfil de {}'.format(self.user.username)