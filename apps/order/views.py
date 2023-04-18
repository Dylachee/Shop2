from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.OrderViewSet):
    serializer_class = OrderSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.pk)
