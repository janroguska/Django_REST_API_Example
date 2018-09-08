from rest_framework.permissions import BasePermission
from .models import Users

class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if isinstance(obj, Users):
			return obj.owner == request.users
		return obj.owner == request.user