from rest_framework import status
from rest_framework.response import Response
from django.db import models
import json


class FilteredListMixin(object):

    LOOKUP_PARAM = '_filter'

    class Meta:
        abstract = True

    @classmethod
    def filter_qs(cls, request, qs):
        try:
            body = json.loads(request.body.strip())
            print(body)
        except Exception:
            body = {}
        
        if FilteredListMixin.LOOKUP_PARAM not in body:
            return qs, status.HTTP_200_OK
        
        try:
            return qs.filter(**body[FilteredListMixin.LOOKUP_PARAM]), status.HTTP_200_OK
        except Exception:
            return None, status.HTTP_400_BAD_REQUEST         


def lego_set_image_filepath(instance, filename):
    return 'img/legosets/{instance.id}/'


def user_avatar_filepath(instance, filename):
    return 'img/avatars/{instance.id}/'

