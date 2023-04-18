from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'confirm':
            self.permissions_classes = [permissions.AllowAny]
        else:
            self.permissions_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.pk)

@action(methods = ['GET'], detail = True)
def confirm(self,request,pk):
    order = Order.objects.get(pk=pk)
    order.status = 'in_process'
    order.save()
    return Response({'message':'Заказ в процессе обработки'}, status=200)

    