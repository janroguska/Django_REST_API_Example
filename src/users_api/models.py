from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import sys

"""Checks the size of the image file, and raises an error
if the file exceeds 150kb
"""
def checkImageSize(image):
	size = sys.getsizeof(image.file)
	limit = 150
	if size > limit * 1024:
		raise ValidationError("Exceeds max size of %sKB" % limit)

"""The model containing the fields that will be included in
the database
"""
class Student(models.Model):
	uid = models.PositiveIntegerField(
		null = False,
		validators = [MinValueValidator(0), MaxValueValidator(999)],
		unique = True
	)
	name = models.CharField(
		max_length = 255,
		null = False
	)
	age = models.PositiveIntegerField(
		null = True,
		validators = [MinValueValidator(0), MaxValueValidator(100)]
	)
	image = models.ImageField(
		upload_to="images/",
		null = True,
		max_length = 100,
		validators = [checkImageSize]
	)
	date_created = models.DateTimeField(
		auto_now_add = True
	)
	date_modified = models.DateTimeField(
		auto_now = True
	)

"""Deletes the image from local storage
"""
@receiver(post_delete, sender=Student)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)
