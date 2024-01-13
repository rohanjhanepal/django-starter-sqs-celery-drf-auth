from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from random import choice
from rest_framework import status
from django.utils import timezone
from users.models import User



'''
## This helps to paginate
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class TicketsViewPaginated(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = 
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user).order_by('-id')
'''