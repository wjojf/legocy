from django.db import models


class TimestampedModel(models.Model):
    '''
    An abstract model that automatically provides `created`,
    `last_modified` fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True