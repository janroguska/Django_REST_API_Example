from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source="owner.username")
	
	class Meta:
		model = Student
		fields = ("uid", "name", "age", "image", "owner", "date_created", "date_modified")
		read_only_fields = ("date_created", "date_modified")

class UserSerializer(serializers.ModelSerializer):
	# student = serializers.PrimaryKeyRelatedField(many=True,
	# 	queryset=Student.objects.all())

	class Meta:
		model = User
		fields = ("id", "username")