import re
from rest_framework.permissions import BasePermission


class IsItemOwner(BasePermission):

    def has_permission(self, request, view, obj):
        return obj.seller == request.user