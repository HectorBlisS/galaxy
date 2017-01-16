from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=140)
	desc = models.TextField()
	