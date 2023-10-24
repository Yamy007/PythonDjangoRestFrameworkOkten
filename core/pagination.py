import math
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total = math.ceil(count/CustomPagination.page_size)
        return Response({
            'total_items':count,
            'total_page': total,
            'current_page': self.page.number,
            'data':data
        }, 200)
