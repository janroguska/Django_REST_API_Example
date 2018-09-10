from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ("uid", "name", "age", "image", "date_created", "date_modified")
		read_only_fields = ("date_created", "date_modified")
