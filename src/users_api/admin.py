from django.contrib import admin
from .models import Student

"""Imports and registers the Student model in the database
"""

admin.site.register(Student)
