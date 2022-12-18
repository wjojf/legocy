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

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                "meta": {
                    'type': 'object',
                    'properties': {
                        "links": {
                            'type': 'object',
                            'properties': {
                                "next": {
                                    'type': "string",
                                    'nullable': True,
                                    'example': "http://localhost:8000/api/v1/series/?page=3",
                                },
                                "previous": {
                                    'type': "string",
                                    'nullable': True,
                                    'example': "http://localhost:8000/api/v1/series/?page=3",
                                },

                            },
                        },
                        "count": {
                            'type': 'integer',
                            'example': 90
                        }
                    },
                },
				"data": schema,
			}
        }
