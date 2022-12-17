from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
    	return Response({
			"meta": {
				'links': {
            		'next': self.get_next_link(),
            		'previous': self.get_previous_link()
        		},
				'count': self.page.paginator.count,
			},
        	'data': data
   	 	})
