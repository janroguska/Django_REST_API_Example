from django.contrib.auth.models import AbstractUser
from django.db import models

"""Object for adding a user to the database.
"""
class CustomUser(AbstractUser):
	name = models.CharField(blank=True, max_length=255)

	def __str__(self):
		return self.username
