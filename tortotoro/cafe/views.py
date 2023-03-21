from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.forms.models import model_to_dict
from .serializers import *
from rest_framework.generics import *

class OrderApiView(ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class SingleOrderView(RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class WorkerApiView(ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer

class SingleWorkerView(RetrieveUpdateDestroyAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer

class WorkerJobApiView(ListCreateAPIView):
    queryset = WorkerJobTitle.objects.all()
    serializer_class = JobSerializer

class SingleWorkerJobView(RetrieveUpdateDestroyAPIView):
    queryset = WorkerJobTitle.objects.all()
    serializer_class = JobSerializer