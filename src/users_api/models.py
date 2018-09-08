from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Users(models.Model):
	uid = models.CharField(max_length=8, null=False)
	name = models.CharField(max_length=255, null=False)
	owner = models.ForeignKey('auth.User', related_name='users',
		on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

def __str__(self):
	return "{}".format(self.uid, self.name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)