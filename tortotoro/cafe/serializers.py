from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerJobTitle
        fields = '__all__'