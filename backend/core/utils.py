from django.db import models


class FilteredListMixin(object):
    def get(self, request, *args, **kwargs):
        try:
            body = json.loads(request.body.strip())
            print(body)
        except Exception as e:
            body = {}

        if 'filter_' in body:
            try:
                self.queryset = self.queryset.filter(**body['filter_'])
            except Exception as e:
                return Response({
                        "data": None,
                        "meta":{
                            "error": 101,
                            "error_message": """
                                Something is wrong with your filters.
                                 Check the 'filter_' param of your request"""
                        }
                    },status=status.HTTP_400_BAD_REQUEST)
    
        
        return super().get(request, *args, **kwargs)


def lego_set_image_filepath(instance, filename):
    return 'img/legosets/{instance.id}/'


def user_avatar_filepath(instance, filename):
    return 'img/avatars/{instance.id}/'

