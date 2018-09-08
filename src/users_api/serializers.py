from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Users
		fields = ("uid", "name", "owner", "date_created", "date_modified")
		read_only_fields = ('date_created', 'date_modified')