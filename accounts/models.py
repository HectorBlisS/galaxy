from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birth = models.DateField(blank=True, null=True)
	tel = models.IntegerField(default=0, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	cover = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

	def __str__(self):
		return 'Perfil de {}'.format(self.user.username)

class Contact(models.Model):
	user_from = models.ForeignKey(User, related_name='rel_from_set')
	user_to = models.ForeignKey(User, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('-created',)

	def _str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)


# Modificamos al modelo User de forma dinamica
User.add_to_class('following',
	models.ManyToManyField('self', 
		through=Contact,
		related_name='followers',
		symmetrical=False))
