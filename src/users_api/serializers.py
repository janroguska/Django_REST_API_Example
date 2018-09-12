from rest_framework import serializers
from .models import Student

"""Uses ModelSerializer to format the Student model, and fields.
"""

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ("uid", "name", "age", "image", "date_created", "date_modified")
		read_only_fields = ("date_created", "date_modified")
