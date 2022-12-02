import re
from rest_framework.permissions import BasePermission


class IsItemOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        return obj.seller == request.user